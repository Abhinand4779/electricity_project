import numpy as np
from datetime import timedelta
from django.utils import timezone
from .models import ElectricityConsumption, EnergyAnomaly

TARIFF_RATE_PER_KWH = 8.00  # Currency units per kWh
CARBON_FACTOR_PER_KWH = 0.82 # kg CO2e per kWh

def analyze_energy_waste(user, days=30):
    """
    Module 6: Energy Waste Analysis
    - Standby / Baseload waste (excessive night idle consumption 00:00 - 05:59)
    - Peak Spikes & Anomalous waste (consumption above expected baseline)
    - Time-of-day usage breakdown (Morning, Afternoon, Evening, Night)
    - Monetary cost wasted and carbon emissions footprint
    """
    cutoff = timezone.now() - timedelta(days=days)
    records = list(ElectricityConsumption.objects.filter(user=user, recorded_at__gte=cutoff).order_by('recorded_at'))

    if not records:
        return {
            'has_data': False,
            'total_consumption': 0.0,
            'estimated_waste_kwh': 0.0,
            'waste_percentage': 0.0,
            'financial_waste': 0.0,
            'carbon_waste_kg': 0.0,
            'baseload_waste_kwh': 0.0,
            'anomaly_waste_kwh': 0.0,
            'peak_waste_kwh': 0.0,
            'period_breakdown': {'Night': 0, 'Morning': 0, 'Afternoon': 0, 'Evening': 0},
            'severity': 'None'
        }

    kwh_vals = [float(r.energy_kwh) for r in records]
    total_consumption = sum(kwh_vals)

    # 1. Period breakdown
    period_kwh = {'Night': 0.0, 'Morning': 0.0, 'Afternoon': 0.0, 'Evening': 0.0}
    night_kwh_list = []

    for r in records:
        hour = r.recorded_at.hour
        val = float(r.energy_kwh)
        if 0 <= hour < 6:
            period_kwh['Night'] += val
            night_kwh_list.append(val)
        elif 6 <= hour < 12:
            period_kwh['Morning'] += val
        elif 12 <= hour < 17:
            period_kwh['Afternoon'] += val
        else:
            period_kwh['Evening'] += val

    # 2. Standby / Baseload Waste
    # In an efficient household, the minimum 15th percentile represents true base load (fridge, router, etc.)
    # Consumption significantly above this during sleeping hours is vampire/standby waste
    baseload_waste = 0.0
    if night_kwh_list:
        min_night_baseline = np.percentile(night_kwh_list, 20)
        # Any night consumption above 1.4x of minimal baseline is considered idle waste
        threshold = max(min_night_baseline * 1.4, min_night_baseline + 0.1)
        baseload_waste = sum(max(0.0, val - threshold) for val in night_kwh_list)

    # 3. Anomaly-driven Waste
    anomalies = EnergyAnomaly.objects.filter(user=user, consumption__recorded_at__gte=cutoff)
    normal_mean = np.mean(kwh_vals)
    anomaly_waste = 0.0

    for anom in anomalies:
        actual_val = float(anom.consumption.energy_kwh)
        if actual_val > normal_mean:
            anomaly_waste += (actual_val - normal_mean)

    # 4. Peak Hour Spikes Waste (Evening 18:00 - 22:00)
    evening_spikes_waste = 0.0
    p85_val = np.percentile(kwh_vals, 85)
    for r in records:
        if 18 <= r.recorded_at.hour <= 22:
            val = float(r.energy_kwh)
            if val > p85_val:
                evening_spikes_waste += (val - p85_val) * 0.5

    total_waste_kwh = round(baseload_waste + (anomaly_waste * 0.7) + evening_spikes_waste, 2)
    # Ensure waste does not exceed total consumption
    total_waste_kwh = min(total_waste_kwh, round(total_consumption * 0.65, 2))

    waste_pct = round((total_waste_kwh / max(total_consumption, 0.01)) * 100, 1)

    financial_waste = round(total_waste_kwh * TARIFF_RATE_PER_KWH, 2)
    carbon_waste_kg = round(total_waste_kwh * CARBON_FACTOR_PER_KWH, 2)

    # Waste severity
    if waste_pct < 12:
        severity = 'Low (Efficient)'
        severity_class = 'severity-low'
    elif waste_pct < 25:
        severity = 'Moderate Inefficiency'
        severity_class = 'severity-moderate'
    elif waste_pct < 40:
        severity = 'High Wastage'
        severity_class = 'severity-high'
    else:
        severity = 'Critical Wastage'
        severity_class = 'severity-critical'

    # Round period breakdown
    for k in period_kwh:
        period_kwh[k] = round(period_kwh[k], 2)

    return {
        'has_data': True,
        'total_consumption': round(total_consumption, 2),
        'estimated_waste_kwh': total_waste_kwh,
        'waste_percentage': waste_pct,
        'financial_waste': financial_waste,
        'carbon_waste_kg': carbon_waste_kg,
        'baseload_waste_kwh': round(baseload_waste, 2),
        'anomaly_waste_kwh': round(anomaly_waste, 2),
        'peak_waste_kwh': round(evening_spikes_waste, 2),
        'period_breakdown': period_kwh,
        'severity': severity,
        'severity_class': severity_class,
        'tariff_rate': TARIFF_RATE_PER_KWH,
        'total_records': len(records)
    }

