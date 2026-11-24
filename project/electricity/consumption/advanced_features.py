import math
from datetime import timedelta
from decimal import Decimal
import numpy as np
from django.utils import timezone
from django.db.models import Avg, Sum, Count, Min, Max

from .models import (
    ElectricityConsumption,
    EnergyAnomaly,
    EnergyRecommendation,
    RecommendationFeedback
)

TARIFF_RATE = 8.00         # ₹ per kWh
CARBON_FACTOR = 0.82       # kg CO2e per kWh


# =====================================================================
# 1. AI ENERGY DIGITAL TWIN & WHAT-IF LIFESTYLE SIMULATOR (Features 01, 03, 06)
# =====================================================================

def simulate_digital_twin(user, solar_kw=0.0, has_ev=False, ev_charging_window='night',
                          ac_upgrade=False, temp_setpoint_shift=0, shift_heavy_loads=False,
                          baseload_cut=False):
    """
    Features 01, 03, 06:
    - 01 AI Energy Digital Twin: Virtual replica of household 24-hr load curve
    - 03 What-If Energy Simulator: Compare baseline vs altered scenarios
    - 06 Future Lifestyle Impact Predictor: Predict impact of EV, Solar, Inverter AC, Setpoint

    Returns 24-hour comparative curves and monthly financial/carbon projections.
    """
    records = list(ElectricityConsumption.objects.filter(user=user).order_by('recorded_at'))

    # Build 24-hour baseline profile
    hourly_buckets = [[] for _ in range(24)]
    if records:
        for r in records:
            hourly_buckets[r.recorded_at.hour].append(float(r.energy_kwh))

    # Standard residential diurnal profile defaults if sparse data
    default_profile = [
        0.28, 0.22, 0.19, 0.18, 0.21, 0.32,  # 00:00 - 05:00 (Night sleep)
        0.58, 0.95, 0.88, 0.65, 0.52, 0.58,  # 06:00 - 11:00 (Morning prep)
        0.62, 0.60, 0.55, 0.58, 0.72, 0.98,  # 12:00 - 17:00 (Afternoon)
        1.45, 1.68, 1.55, 1.25, 0.85, 0.48   # 18:00 - 23:00 (Evening peak)
    ]

    baseline_curve = []
    for h in range(24):
        if len(hourly_buckets[h]) >= 2:
            baseline_curve.append(round(float(np.mean(hourly_buckets[h])), 3))
        else:
            baseline_curve.append(default_profile[h])

    # 1. Solar Rooftop Generation Curve (Bell curve 07:00 - 17:00, peak 12:00 - 13:00)
    solar_curve = [0.0] * 24
    if solar_kw > 0:
        for h in range(7, 18):
            # Normalised sinusoidal curve
            rad = math.pi * (h - 7) / 10.0
            hourly_gen = solar_kw * (math.sin(rad) ** 1.35) * 0.72
            solar_curve[h] = round(max(0.0, hourly_gen), 3)

    # 2. EV Charging Load
    ev_curve = [0.0] * 24
    if has_ev:
        # Typical 3.3 kW home AC charger for 4 hours (~13.2 kWh/day)
        ev_draw = 3.3
        if ev_charging_window == 'night':
            # Off-peak 23:00 - 03:00
            for h in [23, 0, 1, 2]:
                ev_curve[h] = ev_draw
        else:
            # Evening peak 18:00 - 22:00
            for h in [18, 19, 20, 21]:
                ev_curve[h] = ev_draw

    # 3. Simulate New "Digital Twin" Load Curve
    simulated_curve = []
    for h in range(24):
        load = baseline_curve[h]

        # Inverter AC Upgrade: Saves 35% during typical AC hours (12:00 - 16:00, 22:00 - 05:00)
        if ac_upgrade and (12 <= h <= 16 or h >= 22 or h <= 5):
            load = max(0.12, load * 0.65)

        # Thermostat Setpoint Shift: 6% saving per 1°C increase during hot / sleeping hours
        if temp_setpoint_shift > 0 and (12 <= h <= 17 or h >= 22 or h <= 5):
            pct_saving = min(0.20, temp_setpoint_shift * 0.06)
            load = max(0.10, load * (1.0 - pct_saving))

        # Baseload Vampire Standby Cut (00:00 - 05:00)
        if baseload_cut and (0 <= h <= 5):
            load = max(0.10, load * 0.60)

        # Shift Heavy Loads from Evening (19:00 - 21:00) to Solar Midday (12:00 - 14:00)
        if shift_heavy_loads:
            if 19 <= h <= 21:
                load = max(0.25, load - 0.75)
            elif 12 <= h <= 14:
                load = load + 0.75

        # Add EV load
        load = load + ev_curve[h]

        # Offset by Solar Self-Consumption
        net_load = max(0.05, load - solar_curve[h])
        simulated_curve.append(round(net_load, 3))

    # Aggregates (Monthly = 30 days)
    daily_baseline_kwh = sum(baseline_curve)
    daily_simulated_kwh = sum(simulated_curve)
    daily_solar_gen = sum(solar_curve)
    daily_ev_draw = sum(ev_curve)

    monthly_baseline_kwh = round(daily_baseline_kwh * 30, 2)
    monthly_simulated_kwh = round(daily_simulated_kwh * 30, 2)
    monthly_solar_kwh = round(daily_solar_gen * 30, 2)
    monthly_kwh_delta = round(monthly_baseline_kwh - monthly_simulated_kwh, 2)

    monthly_baseline_cost = round(monthly_baseline_kwh * TARIFF_RATE, 2)
    monthly_simulated_cost = round(monthly_simulated_kwh * TARIFF_RATE, 2)
    monthly_cost_savings = round(monthly_baseline_cost - monthly_simulated_cost, 2)
    annual_cost_savings = round(monthly_cost_savings * 12, 2)

    monthly_carbon_reduced_kg = round(monthly_kwh_delta * CARBON_FACTOR, 2)
    annual_carbon_reduced_kg = round(monthly_carbon_reduced_kg * 12, 2)

    # Approximate Capex & Payback
    approx_capex = 0
    if solar_kw > 0:
        approx_capex += solar_kw * 45000  # ₹45k/kW solar rooftop
    if ac_upgrade:
        approx_capex += 38000             # ₹38k 5-star inverter AC

    payback_years = None
    if approx_capex > 0 and annual_cost_savings > 0:
        payback_years = round(approx_capex / annual_cost_savings, 1)

    hour_labels = [f"{h:02d}:00" for h in range(24)]

    return {
        'hour_labels': hour_labels,
        'baseline_curve': baseline_curve,
        'simulated_curve': simulated_curve,
        'solar_curve': solar_curve,
        'ev_curve': ev_curve,
        'daily_baseline_kwh': round(daily_baseline_kwh, 2),
        'daily_simulated_kwh': round(daily_simulated_kwh, 2),
        'monthly_baseline_kwh': monthly_baseline_kwh,
        'monthly_simulated_kwh': monthly_simulated_kwh,
        'monthly_solar_kwh': monthly_solar_kwh,
        'monthly_kwh_delta': monthly_kwh_delta,
        'monthly_baseline_cost': monthly_baseline_cost,
        'monthly_simulated_cost': monthly_simulated_cost,
        'monthly_cost_savings': monthly_cost_savings,
        'annual_cost_savings': annual_cost_savings,
        'monthly_carbon_reduced_kg': monthly_carbon_reduced_kg,
        'annual_carbon_reduced_kg': annual_carbon_reduced_kg,
        'approx_capex': approx_capex,
        'payback_years': payback_years,
        'params': {
            'solar_kw': solar_kw,
            'has_ev': has_ev,
            'ev_charging_window': ev_charging_window,
            'ac_upgrade': ac_upgrade,
            'temp_setpoint_shift': temp_setpoint_shift,
            'shift_heavy_loads': shift_heavy_loads,
            'baseload_cut': baseload_cut
        }
    }


# =====================================================================
# 2. AI ENERGY WASTE DETECTIVE & EXPLAINABLE AI (XAI) (Features 02, 07)
# =====================================================================

def diagnose_waste_detective(user, target_anomaly_id=None):
    """
    Features 02 & 07:
    - 02 AI Energy Waste Detective: Uncovers why unusual consumption happened
    - 07 Explainable AI (XAI): Feature importance attribution & plain-English reasons

    Breaks down anomaly events into root cause culprits:
    - AC compressor drift / stuck thermostat
    - Water heater / geyser left continuous
    - Vampire standby cluster
    - Concurrent multi-appliance overload
    - High thermal heatwave impact
    """
    anomalies = list(
        EnergyAnomaly.objects.filter(user=user)
        .select_related('consumption')
        .order_by('-detected_at')[:20]
    )

    all_user_records = list(ElectricityConsumption.objects.filter(user=user))
    if all_user_records:
        kwh_vals = [float(r.energy_kwh) for r in all_user_records]
        user_mean = float(np.mean(kwh_vals))
        user_std = max(float(np.std(kwh_vals)), 0.1)
        user_p20 = float(np.percentile(kwh_vals, 20))
    else:
        user_mean = 0.8
        user_std = 0.4
        user_p20 = 0.2

    investigations = []

    for anom in anomalies:
        rec = anom.consumption
        kwh = float(rec.energy_kwh)
        hour = rec.recorded_at.hour
        temp = float(rec.temperature) if rec.temperature else 28.0

        # Feature Attribution Weights (XAI)
        # 1. Baseload exceedance factor
        baseload_diff = max(0.0, kwh - user_p20)
        baseload_score = min(50.0, (baseload_diff / max(user_mean, 0.1)) * 30.0)

        # 2. Time-of-Day Context factor (Night hours 00:00 - 05:00 have high anomaly gravity)
        is_night = (0 <= hour <= 5)
        is_peak = (18 <= hour <= 22)
        if is_night:
            tod_score = 35.0
            tod_reason = f"Midnight sleeping hours ({hour:02d}:00) should have minimum idle load"
        elif is_peak:
            tod_score = 25.0
            tod_reason = f"Peak grid window ({hour:02d}:00) subject to heavy simultaneous draws"
        else:
            tod_score = 15.0
            tod_reason = f"Daytime hours ({hour:02d}:00) with moderate expected occupancy"

        # 3. Weather / Thermal Stress factor
        if temp >= 33.0:
            thermal_score = min(30.0, (temp - 30.0) * 4.0)
            thermal_reason = f"Extreme ambient heat ({temp:.1f}°C) heavily stressed HVAC compressors"
        elif temp <= 16.0:
            thermal_score = min(25.0, (18.0 - temp) * 3.5)
            thermal_reason = f"Low ambient temperature ({temp:.1f}°C) likely drove space/water heating"
        else:
            thermal_score = 8.0
            thermal_reason = f"Mild weather ({temp:.1f}°C); thermal load cannot justify spike"

        # 4. Spike Suddenness (Z-Score)
        z_score = max(0.0, (kwh - user_mean) / user_std)
        spike_score = min(30.0, z_score * 8.0)

        total_raw = baseload_score + tod_score + thermal_score + spike_score
        if total_raw == 0:
            total_raw = 1.0

        attr_baseload = round((baseload_score / total_raw) * 100, 1)
        attr_tod = round((tod_score / total_raw) * 100, 1)
        attr_thermal = round((thermal_score / total_raw) * 100, 1)
        attr_spike = round((spike_score / total_raw) * 100, 1)

        # Appliance Signature Disaggregation
        if is_night and kwh > 1.2:
            culprit_name = "Air Conditioner Compressor Continuous Cycling / Thermostat Bypass"
            culprit_icon = "❄️"
            culprit_type = "Equipment Inefficiency / Malfunction"
            confidence = 94
            explanation = (
                f"Recorded {kwh:.2f} kWh at {hour:02d}:00 during sleep hours. While the baseline expectation is "
                f"{user_p20:.2f} kWh, the AC compressor ran continuously without cycling down. Possible low refrigerant "
                f"or door/window seal leakage."
            )
            action = "Inspect AC refrigerant levels and verify room weatherstripping/door seals."
            estimated_waste = round(max(0.0, kwh - user_p20), 2)

        elif (6 <= hour <= 10 or 17 <= hour <= 21) and kwh > 2.8:
            culprit_name = "Electric Geyser / Water Heater Left Continuously ON"
            culprit_icon = "♨️"
            culprit_type = "Behavioral Waste"
            confidence = 91
            explanation = (
                f"Massive continuous draw of {kwh:.2f} kWh matches a 2000W-3000W immersion heating element running non-stop. "
                f"Standard showers require 15-20 minutes, whereas this cycle consumed {kwh:.2f} kWh in a single hour."
            )
            action = "Install a smart geyser timer to automatically shut off power after 25 minutes."
            estimated_waste = round(kwh * 0.70, 2)

        elif is_night and 0.45 <= kwh <= 1.2:
            culprit_name = "Vampire / Phantom Standby Cluster & Refrigeration Seal Wear"
            culprit_icon = "🧛"
            culprit_type = "Standby Parasitic Loss"
            confidence = 88
            explanation = (
                f"Overnight baseline remained at {kwh:.2f} kWh, which is {round(kwh / max(user_p20, 0.05), 1)}x higher "
                f"than the true idle floor ({user_p20:.2f} kWh). Likely caused by always-on gaming PCs, entertainment amplifiers, "
                f"and worn refrigerator door gaskets."
            )
            action = "Deploy master cutoff power strips for entertainment hubs and check refrigerator magnetic seal."
            estimated_waste = round(max(0.0, kwh - user_p20 * 1.5), 2)

        elif kwh > 3.8:
            culprit_name = "Simultaneous Heavy Appliance Peak Overload"
            culprit_icon = "⚡"
            culprit_type = "Concurrent Peak Congestion"
            confidence = 96
            explanation = (
                f"Exceptional spike of {kwh:.2f} kWh (+{round(z_score, 1)}σ standard deviations). "
                f"Occurred during {hour:02d}:00 when high-wattage equipment (Microwave, Induction Cooktop, AC, and Iron) "
                f"were activated simultaneously."
            )
            action = "Stagger usage of inductive cooking and laundry away from peak cooling hours."
            estimated_waste = round(kwh * 0.45, 2)

        else:
            culprit_name = "Thermal Resistance Stress (Extreme Ambient Delta)"
            culprit_icon = "🌡️"
            culprit_type = "Weather Dependency"
            confidence = 85
            explanation = (
                f"Spike of {kwh:.2f} kWh strongly correlates with outdoor temperature ({temp:.1f}°C). "
                f"Heat ingress caused cooling appliances to draw 40% more current to maintain target setpoints."
            )
            action = "Draw thermal curtains during peak sun hours and adjust thermostat to 25°C."
            estimated_waste = round(kwh * 0.30, 2)

        investigations.append({
            'anomaly_id': anom.id,
            'recorded_at': rec.recorded_at,
            'kwh': kwh,
            'hour': hour,
            'temperature': temp,
            'culprit_name': culprit_name,
            'culprit_icon': culprit_icon,
            'culprit_type': culprit_type,
            'confidence': confidence,
            'explanation': explanation,
            'action': action,
            'estimated_waste': estimated_waste,
            'is_resolved': anom.is_resolved,
            'xai_attributions': {
                'baseload': attr_baseload,
                'time_of_day': attr_tod,
                'thermal': attr_thermal,
                'spike_rate': attr_spike
            }
        })

    # Pick focused incident
    selected_incident = None
    if target_anomaly_id:
        selected_incident = next((inv for inv in investigations if inv['anomaly_id'] == target_anomaly_id), None)
    if not selected_incident and investigations:
        selected_incident = investigations[0]

    return {
        'investigations': investigations,
        'selected_incident': selected_incident,
        'total_anomalies_investigated': len(investigations),
        'user_mean_kwh': round(user_mean, 2),
        'user_baseline_idle': round(user_p20, 2),
    }


# =====================================================================
# 3. PERSONAL ENERGY FINGERPRINT (Feature 05)
# =====================================================================

def compute_energy_fingerprint(user):
    """
    Feature 05 Personal Energy Fingerprint:
    Generates an individual energy behavioral profile:
    - Night Owl Score (00:00 - 06:00 usage ratio)
    - Baseload Ratio (vampire load vs average load)
    - Weekend Surge Index (weekend vs weekday usage ratio)
    - Weather Elasticity (temperature correlation)
    - Peak Hour Discipline (avoidance of 18:00 - 22:00)

    Assigns a behavioral archetype and radar chart metrics.
    """
    records = list(ElectricityConsumption.objects.filter(user=user))

    if not records:
        return {
            'has_data': False,
            'archetype_name': 'New Energy Consumer',
            'archetype_badge': '🌱 New Household',
            'archetype_description': 'Please import or record usage history to generate your personalized Energy DNA.',
            'radar_labels': ['Night Owl', 'Baseload Control', 'Weekend Discipline', 'Peak Avoidance', 'Weather Resilience'],
            'user_radar': [50, 50, 50, 50, 50],
            'benchmark_radar': [40, 70, 60, 65, 60],
            'fingerprint_score': 50,
            'traits': []
        }

    kwh_list = [float(r.energy_kwh) for r in records]
    total_kwh = sum(kwh_list)
    avg_kwh = total_kwh / len(records)

    # 1. Night Owl Metric (00:00 - 05:59)
    night_kwh = sum(float(r.energy_kwh) for r in records if 0 <= r.recorded_at.hour <= 5)
    night_ratio = (night_kwh / max(total_kwh, 0.1)) * (24.0 / 6.0) # Normalized against 25% equal split
    # Score 0 (extreme night owl) to 100 (exemplary sleep conservation)
    night_discipline_score = max(10, min(95, round(100 - (night_ratio - 0.5) * 60)))

    # 2. Baseload Control (20th percentile idle / mean)
    p20_idle = float(np.percentile(kwh_list, 20))
    baseload_ratio = p20_idle / max(avg_kwh, 0.05)
    # Good baseload is < 0.35 of average
    baseload_score = max(15, min(95, round(100 - (baseload_ratio * 120))))

    # 3. Weekend Surge Index
    weekday_kwh = [float(r.energy_kwh) for r in records if r.recorded_at.weekday() < 5]
    weekend_kwh = [float(r.energy_kwh) for r in records if r.recorded_at.weekday() >= 5]
    avg_weekday = np.mean(weekday_kwh) if weekday_kwh else avg_kwh
    avg_weekend = np.mean(weekend_kwh) if weekend_kwh else avg_kwh
    weekend_surge_ratio = float(avg_weekend) / max(float(avg_weekday), 0.05)
    weekend_discipline_score = max(15, min(95, round(100 - abs(weekend_surge_ratio - 1.0) * 80)))

    # 4. Peak Hour Avoidance (18:00 - 22:00)
    peak_kwh = sum(float(r.energy_kwh) for r in records if 18 <= r.recorded_at.hour <= 22)
    peak_share = (peak_kwh / max(total_kwh, 0.1)) * (24.0 / 5.0)
    peak_avoidance_score = max(15, min(95, round(100 - (peak_share - 0.7) * 70)))

    # 5. Weather / Temperature Elasticity
    temp_pairs = [(float(r.energy_kwh), float(r.temperature)) for r in records if r.temperature is not None]
    if len(temp_pairs) >= 5:
        kwh_arr = [p[0] for p in temp_pairs]
        tmp_arr = [p[1] for p in temp_pairs]
        corr = np.corrcoef(kwh_arr, tmp_arr)[0, 1]
        if np.isnan(corr):
            corr = 0.3
    else:
        corr = 0.35
    weather_resilience_score = max(15, min(95, round(100 - max(0.0, corr) * 80)))

    # Overall Fingerprint Efficiency Score (0-100)
    fingerprint_score = round(
        (night_discipline_score * 0.25) +
        (baseload_score * 0.25) +
        (weekend_discipline_score * 0.15) +
        (peak_avoidance_score * 0.20) +
        (weather_resilience_score * 0.15)
    )

    # Determine Behavioral Archetype
    if solar_candidate := (peak_share < 1.1 and night_ratio < 0.8 and avg_weekday > 0.6):
        archetype_name = "Solar-Ready Daylight Household"
        archetype_badge = "☀️ Solar-Ready Prime"
        archetype_description = (
            "Your peak energy consumption directly coincides with abundant daylight solar production. "
            "Installing rooftop solar would immediately offset 65-80% of your current grid tariff."
        )
    elif night_ratio > 1.3:
        archetype_name = "Night Owl Digital Household"
        archetype_badge = "🦉 Night-Heavy Consumer"
        archetype_description = (
            "Substantial electricity consumption occurs between 00:00 and 06:00. Likely driven by late-night "
            "computing, entertainment hubs, or AC running at low setpoints."
        )
    elif weather_resilience_score < 40:
        archetype_name = "Climate-Sensitive HVAC Household"
        archetype_badge = "❄️ Thermal Dependent"
        archetype_description = (
            "Your electricity demand fluctuates heavily with ambient heat. Inverter AC upgrades and smart "
            "thermal curtains will offer dramatic bill reductions."
        )
    elif weekend_surge_ratio > 1.35:
        archetype_name = "Weekend Heavy Concentrator"
        archetype_badge = "⚡ Weekend Surge Living"
        archetype_description = (
            "Weekdays show disciplined low usage, but Saturdays and Sundays exhibit a +35% surge in appliance "
            "batches (washing, ironing, continuous entertainment)."
        )
    else:
        archetype_name = "Balanced Eco-Conscious Household"
        archetype_badge = "🌿 Balanced Eco-Profile"
        archetype_description = (
            "Consistent daily rhythm, minimal nocturnal vampire drain, and controlled baseload. A prime model "
            "of efficient modern residential energy consumption."
        )

    # Persona Behavioral Traits
    traits = [
        {
            'name': 'Nighttime Sleep Idle',
            'value': f"{round(night_kwh / max(total_kwh, 0.01) * 100, 1)}%",
            'status': 'Optimal' if night_discipline_score >= 65 else 'High Idle',
            'score': night_discipline_score
        },
        {
            'name': 'Baseload Standby Floor',
            'value': f"{round(p20_idle, 2)} kWh/h",
            'status': 'Tight' if baseload_score >= 65 else 'Vampire Leakage',
            'score': baseload_score
        },
        {
            'name': 'Weekend vs Weekday Ratio',
            'value': f"{round(weekend_surge_ratio, 2)}x",
            'status': 'Even Rhythm' if weekend_discipline_score >= 65 else 'Weekend Heavy',
            'score': weekend_discipline_score
        },
        {
            'name': 'Evening Peak Share',
            'value': f"{round(peak_kwh / max(total_kwh, 0.01) * 100, 1)}%",
            'status': 'Discipline' if peak_avoidance_score >= 65 else 'Congested',
            'score': peak_avoidance_score
        },
        {
            'name': 'Thermal / Weather Sensitivity',
            'value': f"{round(max(0.0, corr) * 100, 0)}%",
            'status': 'Resilient' if weather_resilience_score >= 65 else 'HVAC Dependent',
            'score': weather_resilience_score
        }
    ]

    return {
        'has_data': True,
        'archetype_name': archetype_name,
        'archetype_badge': archetype_badge,
        'archetype_description': archetype_description,
        'fingerprint_score': fingerprint_score,
        'radar_labels': ['Night Conservation', 'Baseload Control', 'Weekend Rhythm', 'Peak Avoidance', 'Weather Resilience'],
        'user_radar': [
            night_discipline_score,
            baseload_score,
            weekend_discipline_score,
            peak_avoidance_score,
            weather_resilience_score
        ],
        'benchmark_radar': [55, 60, 65, 50, 55],
        'ideal_radar': [85, 90, 85, 80, 85],
        'traits': traits,
        'total_analyzed_hours': len(records),
        'average_kwh_per_hour': round(avg_kwh, 3),
        'idle_floor_kwh': round(p20_idle, 3)
    }


# =====================================================================
# 4. SELF-LEARNING RECOMMENDATION ENGINE (Feature 04)
# =====================================================================

def record_user_feedback(user, recommendation_id, feedback_type, note=''):
    """
    Feature 04 Self-Learning Recommendation Engine:
    Updates recommendation priority weight using reinforcement feedback:
    - 'helpful': +40% weight boost
    - 'already_done': Mark completed, suppress repeat, unlock higher-level saving
    - 'not_feasible': -60% weight reduction, prioritize alternative actions
    """
    rec = EnergyRecommendation.objects.filter(user=user, id=recommendation_id).first()
    if not rec:
        return None

    # Record feedback audit
    feedback = RecommendationFeedback.objects.create(
        user=user,
        recommendation=rec,
        feedback_type=feedback_type,
        feedback_note=note
    )

    rec.feedback_status = feedback_type

    if feedback_type == 'helpful':
        rec.priority_weight = min(2.5, rec.priority_weight * 1.4)
    elif feedback_type == 'already_done':
        rec.is_completed = True
        rec.priority_weight = 0.5
    elif feedback_type == 'not_feasible':
        rec.priority_weight = max(0.1, rec.priority_weight * 0.4)

    rec.save()
    return feedback


def get_self_learning_metrics(user):
    """
    Computes adaptation metrics of the self-learning engine.
    """
    all_recs = EnergyRecommendation.objects.filter(user=user)
    feedbacks = RecommendationFeedback.objects.filter(user=user)

    total_tips = all_recs.count()
    completed_tips = all_recs.filter(is_completed=True).count()
    feedback_count = feedbacks.count()

    # Self-learning calibration level (starts at 60%, approaches 98% with user interactions)
    calibration_score = min(98, 60 + (feedback_count * 8))

    return {
        'total_tips': total_tips,
        'completed_tips': completed_tips,
        'feedback_count': feedback_count,
        'calibration_score': calibration_score,
        'recent_feedbacks': feedbacks.select_related('recommendation')[:5]
    }

