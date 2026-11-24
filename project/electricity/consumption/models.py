from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# 1. Electricity Consumption Model
class ElectricityConsumption(models.Model):

    SOURCE_CHOICES = [
        ('manual', 'Manual Entry'),
        ('dataset', 'Dataset Import'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='consumption_records'
    )

    recorded_at = models.DateTimeField()

    energy_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)]
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default='manual'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']
        indexes = [
            models.Index(fields=['user', 'recorded_at']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.energy_kwh} kWh"


# 2. Consumption Prediction Model
class ConsumptionPrediction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    target_date = models.DateField()

    predicted_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)]
    )

    algorithm = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_kwh} kWh"


# 3. Energy Anomaly Model
class EnergyAnomaly(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    consumption = models.ForeignKey(
        ElectricityConsumption,
        on_delete=models.CASCADE,
        related_name='anomalies'
    )

    anomaly_score = models.FloatField()

    description = models.TextField()

    detected_at = models.DateTimeField(auto_now_add=True)

    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Anomaly - {self.user.username}"


# 4. Energy Recommendation Model
class EnergyRecommendation(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    estimated_saving_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        default=0,
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_completed = models.BooleanField(default=False)

    FEEDBACK_CHOICES = [
        ('pending', 'Pending Review'),
        ('helpful', 'Helpful & Implemented'),
        ('already_done', 'Already Doing This'),
        ('not_feasible', 'Not Feasible'),
    ]

    feedback_status = models.CharField(
        max_length=20,
        choices=FEEDBACK_CHOICES,
        default='pending'
    )

    priority_weight = models.FloatField(default=1.0)

    def __str__(self):
        return self.title


# 4b. Recommendation Feedback Model (Self-Learning Feedback Loop)
class RecommendationFeedback(models.Model):

    FEEDBACK_CHOICES = [
        ('helpful', 'Helpful & Implemented'),
        ('already_done', 'Already Doing This'),
        ('not_feasible', 'Not Feasible'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendation_feedbacks'
    )

    recommendation = models.ForeignKey(
        EnergyRecommendation,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    feedback_type = models.CharField(
        max_length=20,
        choices=FEEDBACK_CHOICES
    )

    feedback_note = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.recommendation.title}: {self.feedback_type}"


# 5. Energy Efficiency Score Model
class EnergyEfficiencyScore(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    period_start = models.DateField()

    period_end = models.DateField()

    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/100"
