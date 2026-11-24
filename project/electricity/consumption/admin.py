
from django.contrib import admin
from .models import (
    ElectricityConsumption,
    ConsumptionPrediction,
    EnergyAnomaly,
    EnergyRecommendation,
    EnergyEfficiencyScore,
    RecommendationFeedback
)


@admin.register(ElectricityConsumption)
class ElectricityConsumptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'recorded_at', 'energy_kwh', 'source')
    list_filter = ('source', 'recorded_at')
    search_fields = ('user__username',)


@admin.register(ConsumptionPrediction)
class ConsumptionPredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_date', 'predicted_kwh', 'algorithm')


@admin.register(EnergyAnomaly)
class EnergyAnomalyAdmin(admin.ModelAdmin):
    list_display = ('user', 'anomaly_score', 'detected_at', 'is_resolved')
    list_filter = ('is_resolved',)


@admin.register(EnergyRecommendation)
class EnergyRecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_completed', 'feedback_status', 'priority_weight')
    list_filter = ('is_completed', 'feedback_status')


@admin.register(RecommendationFeedback)
class RecommendationFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation', 'feedback_type', 'created_at')
    list_filter = ('feedback_type', 'created_at')


@admin.register(EnergyEfficiencyScore)
class EnergyEfficiencyScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'period_start', 'period_end')
