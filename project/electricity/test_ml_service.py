
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "electricity.settings"
)

django.setup()

from consumption.ml_service import detect_anomaly


sample = {
    "Electricity_Consumed": 0.95,
    "Temperature": 0.50,
    "Humidity": 0.45,
    "Wind_Speed": 0.40,
    "Avg_Past_Consumption": 0.35,
    "Hour": 12,
    "Day": 14,
    "DayOfWeek": 6,
    "Month": 4,
    "IsWeekend": 1
}

result = detect_anomaly(sample)

print("\n========== ANOMALY RESULT ==========")
print(result)
