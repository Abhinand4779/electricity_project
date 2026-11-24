from decimal import Decimal
from django.utils import timezone
from .models import EnergyRecommendation, EnergyAnomaly
from .waste_analysis import analyze_energy_waste

DEFAULT_RECOMMENDATIONS = [
    {
        'title': 'Minimize Nighttime Standby / Vampire Load',
        'description': 'Smart plugs or master power strips can power down entertainment centers, computing equipment, and chargers overnight (12:00 AM – 6:00 AM).',
        'base_savings': 1.8
    },
    {
        'title': 'Shift Heavy Appliances to Off-Peak Hours',
        'description': 'Run washing machines, dishwashers, and water heaters during solar off-peak hours (11:00 AM – 4:00 PM) rather than peak evening hours (6:00 PM – 10:00 PM).',
        'base_savings': 2.5
    },
    {
        'title': 'Optimize AC / Heating Thermostat Setpoint',
        'description': 'Adjust cooling temperature to 24°C–25°C in summer. Every 1°C increase in AC setpoint saves approximately 6% of cooling energy consumption.',
        'base_savings': 3.2
    },
    {
        'title': 'Resolve Unmonitored High Energy Spikes',
        'description': 'Inspect devices causing unexpected consumption spikes detected by AI anomaly analysis to verify faulty thermostats or unneeded concurrent loads.',
        'base_savings': 2.0
    },
    {
        'title': 'Implement Scheduled LED Lighting & Timers',
        'description': 'Install motion sensors and automated sunset timers for outdoor and hallway lighting to prevent inadvertent daytime illumination.',
        'base_savings': 1.2
    }
]

def generate_personalized_recommendations(user):
    """
    Module 7: Energy-Saving Recommendation Engine
    - Generates personalized recommendations based on the user's actual waste analysis
    - Calculates customized estimated kWh savings
    - Syncs into EnergyRecommendation model
    - Generates an optimal Energy-Saving Appliance Schedule
    """
    waste_data = analyze_energy_waste(user, days=30)
    est_waste = waste_data.get('estimated_waste_kwh', 0)

    # Determine personalized savings multipliers based on user waste
    multiplier = max(0.8, min(est_waste / 20.0, 3.5)) if est_waste > 0 else 1.0

    existing_titles = set(EnergyRecommendation.objects.filter(user=user).values_list('title', flat=True))

    new_recommendations = []
    for item in DEFAULT_RECOMMENDATIONS:
        if item['title'] not in existing_titles:
            custom_savings = round(item['base_savings'] * multiplier, 2)
            new_recommendations.append(
                EnergyRecommendation(
                    user=user,
                    title=item['title'],
                    description=item['description'],
                    estimated_saving_kwh=Decimal(str(custom_savings)),
                    is_completed=False
                )
            )

    if new_recommendations:
        EnergyRecommendation.objects.bulk_create(new_recommendations)

    user_recommendations = list(
        EnergyRecommendation.objects.filter(user=user)
        .order_by('is_completed', '-priority_weight', '-estimated_saving_kwh')
    )

    total_potential_savings = sum(float(r.estimated_saving_kwh) for r in user_recommendations if not r.is_completed)
    completed_savings = sum(float(r.estimated_saving_kwh) for r in user_recommendations if r.is_completed)

    # Recommended Appliance Schedule Table
    schedule = [
        {
            'appliance': 'Washing Machine & Dryer',
            'suggested_time': '10:00 AM - 02:00 PM',
            'reason': 'Solar generation peak / Off-peak grid tariff',
            'impact': 'High (Saves up to 25% peak charges)'
        },
        {
            'appliance': 'Dishwasher',
            'suggested_time': '01:00 PM - 04:00 PM',
            'reason': 'Avoids dinner peak grid surge (06:00 PM - 09:00 PM)',
            'impact': 'Medium'
        },
        {
            'appliance': 'Air Conditioner / Heat Pump',
            'suggested_time': 'Pre-cool 03:00 PM, Set 25°C at Night',
            'reason': 'Pre-cooling prevents high-draw cycling during heat peaks',
            'impact': 'Very High (15-20% overall reduction)'
        },
        {
            'appliance': 'Electric Water Heater (Geyser)',
            'suggested_time': 'Timer 06:00 AM - 08:00 AM only',
            'reason': 'Prevents 24/7 continuous standby reheating losses',
            'impact': 'High (1.5 - 3 kWh/day)'
        },
        {
            'appliance': 'EV / Battery Charging',
            'suggested_time': '11:00 PM - 05:00 AM',
            'reason': 'Utilizes lowest overnight off-peak tariff',
            'impact': 'Very High'
        }
    ]

    return {
        'recommendations': user_recommendations,
        'total_potential_savings': round(total_potential_savings, 2),
        'completed_savings': round(completed_savings, 2),
        'financial_savings': round(total_potential_savings * 8.0, 2),
        'schedule': schedule
    }

