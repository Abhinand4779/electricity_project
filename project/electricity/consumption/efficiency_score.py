from datetime import timedelta
from decimal import Decimal
import numpy as np
from django.utils import timezone
from .models import ElectricityConsumption, EnergyAnomaly, EnergyEfficiencyScore

def calculate_energy_efficiency_score(user, days=30):
    """
    Module 8 & Section 6.6: Personalised Energy-Efficiency Score (0 to 100)
    
    Evaluates:
    1. Anomaly Penalty (up to 35 pts): High proportion of abnormal records reduces score.
    2. Baseload / Night Inefficiency Penalty (up to 25 pts): Excessive night consumption (00:00-06:00).
    3. Peak-to-Average Ratio Penalty (up to 25 pts): High peak spikes vs median consumption.
    4. Volatility / Stability Bonus (up to 15 pts): Smooth, predictable usage habits.
    """
    cutoff = timezone.now() - timedelta(days=days)
    records = ElectricityConsumption.objects.filter(user=user, recorded_at__gte=cutoff).order_by('recorded_at')
    total_records = records.count()

    if total_records < 3:
        # Default starting score when insufficient data
        return {
            'score': 75,
            'grade': 'B',
            'status': 'Baseline Established',
            'breakdown': {
                'anomaly_points': 30,
                'baseload_points': 20,
                'peak_points': 18,
                'stability_points': 7
            },
            'has_sufficient_data': False,
            'message': 'Record at least 3 consumption entries to unlock your personalized AI efficiency score.'
        }

    kwh_list = [float(r.energy_kwh) for r in records]
    hours = [r.recorded_at.hour for r in records]

    # 1. Anomaly factor
    anomaly_count = EnergyAnomaly.objects.filter(user=user, consumption__recorded_at__gte=cutoff).count()
    anomaly_ratio = anomaly_count / max(total_records, 1)
    # 0 anomalies = 35 pts, 20%+ anomalies = 5 pts
    anomaly_points = max(5, int(35 * (1 - min(anomaly_ratio * 4.0, 0.85))))

    # 2. Baseload / Night waste factor (hours 0 to 5)
    night_kwh = [kwh for kwh, h in zip(kwh_list, hours) if 0 <= h < 6]
    day_kwh = [kwh for kwh, h in zip(kwh_list, hours) if 6 <= h < 24]

    avg_night = np.mean(night_kwh) if night_kwh else 0
    avg_day = np.mean(day_kwh) if day_kwh else (np.mean(kwh_list) if kwh_list else 1)

    # In efficient homes, night baseload is typically 20-35% of daytime average.
    night_ratio = (avg_night / max(avg_day, 0.01))
    if night_ratio <= 0.35:
        baseload_points = 25
    elif night_ratio <= 0.60:
        baseload_points = 18
    elif night_ratio <= 0.85:
        baseload_points = 12
    else:
        baseload_points = 6

    # 3. Peak-to-Average Ratio
    mean_val = np.mean(kwh_list)
    p95_val = np.percentile(kwh_list, 95)
    peak_ratio = p95_val / max(mean_val, 0.01)

    if peak_ratio <= 1.8:
        peak_points = 25
    elif peak_ratio <= 2.5:
        peak_points = 19
    elif peak_ratio <= 3.5:
        peak_points = 12
    else:
        peak_points = 5

    # 4. Usage Volatility / Consistency
    std_val = np.std(kwh_list)
    cov = std_val / max(mean_val, 0.01) # Coefficient of variation
    if cov <= 0.40:
        stability_points = 15
    elif cov <= 0.75:
        stability_points = 11
    elif cov <= 1.20:
        stability_points = 7
    else:
        stability_points = 3

    total_score = min(100, max(15, anomaly_points + baseload_points + peak_points + stability_points))

    # Grade determination
    if total_score >= 88:
        grade = 'A+'
        status = 'Excellent Efficiency'
    elif total_score >= 78:
        grade = 'A'
        status = 'High Efficiency'
    elif total_score >= 65:
        grade = 'B'
        status = 'Moderate Efficiency'
    elif total_score >= 50:
        grade = 'C'
        status = 'Needs Optimization'
    else:
        grade = 'D'
        status = 'High Energy Wastage'

    # Store or update in database
    period_start = records.first().recorded_at.date()
    period_end = records.last().recorded_at.date()

    EnergyEfficiencyScore.objects.update_or_create(
        user=user,
        period_start=period_start,
        period_end=period_end,
        defaults={'score': total_score}
    )

    return {
        'score': total_score,
        'grade': grade,
        'status': status,
        'breakdown': {
            'anomaly_points': anomaly_points,
            'baseload_points': baseload_points,
            'peak_points': peak_points,
            'stability_points': stability_points
        },
        'has_sufficient_data': True,
        'total_analyzed': total_records,
        'anomalies_detected': anomaly_count
    }

