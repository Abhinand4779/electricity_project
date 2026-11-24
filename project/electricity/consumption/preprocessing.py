import io
import csv
import pandas as pd
from datetime import datetime
from decimal import Decimal
from django.utils import timezone
from .models import ElectricityConsumption

def get_usage_period(hour):
    """
    Categorize hour of day into academic usage periods:
    Night (00:00-05:59), Morning (06:00-11:59), Afternoon (12:00-16:59), Evening (17:00-23:59)
    """
    if 0 <= hour < 6:
        return 'Night'
    elif 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    else:
        return 'Evening'

def clean_and_preprocess_dataframe(df):
    """
    Module 3: Data Preprocessing
    - Remove duplicate records
    - Handle missing values
    - Identify and filter incorrect data
    - Extract calendar, time-series, and usage period features
    """
    summary = {
        'initial_count': len(df),
        'duplicates_removed': 0,
        'missing_values_handled': 0,
        'invalid_records_dropped': 0,
        'final_count': 0
    }

    # Normalize column names
    col_mapping = {}
    for col in df.columns:
        c_clean = col.strip().lower().replace(' ', '_')
        if c_clean in ['timestamp', 'recorded_at', 'date', 'datetime']:
            col_mapping[col] = 'recorded_at'
        elif c_clean in ['electricity_consumed', 'energy_kwh', 'consumption', 'power', 'kwh', 'energy']:
            col_mapping[col] = 'energy_kwh'
        elif c_clean in ['temperature', 'temp']:
            col_mapping[col] = 'temperature'
        elif c_clean in ['humidity']:
            col_mapping[col] = 'humidity'
        elif c_clean in ['wind_speed', 'windspeed']:
            col_mapping[col] = 'wind_speed'
        elif c_clean in ['avg_past_consumption', 'past_consumption']:
            col_mapping[col] = 'avg_past_consumption'

    df = df.rename(columns=col_mapping)

    if 'recorded_at' not in df.columns or 'energy_kwh' not in df.columns:
        raise ValueError("Dataset must contain a date/timestamp column and an electricity consumption (kWh) column.")

    # 1. Parse timestamps and drop unparseable
    df['recorded_at'] = pd.to_datetime(df['recorded_at'], errors='coerce')
    invalid_dates = df['recorded_at'].isna().sum()
    df = df.dropna(subset=['recorded_at'])

    # 2. Convert energy_kwh to numeric
    df['energy_kwh'] = pd.to_numeric(df['energy_kwh'], errors='coerce')
    invalid_energy = df['energy_kwh'].isna().sum() + (df['energy_kwh'] < 0).sum()
    df = df[df['energy_kwh'].notna() & (df['energy_kwh'] >= 0)]

    # 3. Deduplication
    init_len = len(df)
    df = df.drop_duplicates(subset=['recorded_at'])
    summary['duplicates_removed'] = int(init_len - len(df))

    # 4. Handle temperature if present
    if 'temperature' in df.columns:
        df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
        # Impute missing temperature with median or forward fill
        missing_temp = df['temperature'].isna().sum()
        if missing_temp > 0:
            df['temperature'] = df['temperature'].fillna(df['temperature'].median() if not df['temperature'].dropna().empty else 22.0)
            summary['missing_values_handled'] += int(missing_temp)

    # 5. Extract time-series features
    df['hour'] = df['recorded_at'].dt.hour
    df['day'] = df['recorded_at'].dt.day
    df['day_of_week'] = df['recorded_at'].dt.dayofweek
    df['month'] = df['recorded_at'].dt.month
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
    df['usage_period'] = df['hour'].apply(get_usage_period)

    # Sort chronologically
    df = df.sort_values('recorded_at').reset_index(drop=True)

    summary['invalid_records_dropped'] = int(invalid_dates + invalid_energy)
    summary['final_count'] = len(df)

    return df, summary

def import_records_from_csv(file_obj, user, source='dataset'):
    """
    Parses an uploaded CSV file, cleans the data, and bulk creates ElectricityConsumption records.
    """
    content = file_obj.read()
    if isinstance(content, bytes):
        content = content.decode('utf-8-sig', errors='replace')

    csv_file = io.StringIO(content)
    df = pd.read_csv(csv_file)

    cleaned_df, summary = clean_and_preprocess_dataframe(df)

    # Existing timestamps for this user to prevent database duplicates
    existing_timestamps = set(
        ElectricityConsumption.objects.filter(user=user).values_list('recorded_at', flat=True)
    )

    records_to_create = []
    skipped_existing = 0

    for _, row in cleaned_df.iterrows():
        rec_time = row['recorded_at']
        if timezone.is_naive(rec_time):
            rec_time = timezone.make_aware(rec_time, timezone.utc)

        if rec_time in existing_timestamps:
            skipped_existing += 1
            continue

        temp_val = None
        if 'temperature' in row and pd.notna(row['temperature']):
            temp_val = Decimal(str(round(float(row['temperature']), 2)))

        energy_val = Decimal(str(round(float(row['energy_kwh']), 3)))

        records_to_create.append(ElectricityConsumption(
            user=user,
            recorded_at=rec_time,
            energy_kwh=energy_val,
            temperature=temp_val,
            source=source
        ))

    if records_to_create:
        ElectricityConsumption.objects.bulk_create(records_to_create, batch_size=500)

    summary['created_count'] = len(records_to_create)
    summary['skipped_existing'] = skipped_existing

    return summary

def import_sample_dataset_for_user(user, sample_type='household', limit=168):
    """
    Imports realistic historical records for user (default 168 records = 1 full week of hourly data).
    sample_type: 'household' or 'smart_meter'
    """
    import os
    from django.conf import settings

    if sample_type == 'household':
        file_path = os.path.join(settings.BASE_DIR, 'datasets', 'household_hourly_consumption.csv')
    else:
        file_path = os.path.join(settings.BASE_DIR, 'datasets', 'smart_meter_data.csv')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Sample dataset file not found at {file_path}")

    df = pd.read_csv(file_path)

    # Map column names
    if 'Timestamp' in df.columns:
        df = df.rename(columns={'Timestamp': 'recorded_at', 'Electricity_Consumed': 'energy_kwh'})

    df, _ = clean_and_preprocess_dataframe(df)

    # Take the latest `limit` records
    sample_df = df.tail(limit).copy()

    # Re-anchor dates so they appear in recent days up to today
    now = timezone.now()
    if not sample_df.empty:
        hours_back = list(range(len(sample_df) - 1, -1, -1))
        sample_df['recorded_at'] = [
            (now - pd.Timedelta(hours=h)).replace(minute=0, second=0, microsecond=0)
            for h in hours_back
        ]

    # Delete previous sample records if any, or just import
    existing_timestamps = set(
        ElectricityConsumption.objects.filter(user=user).values_list('recorded_at', flat=True)
    )

    records = []
    for _, row in sample_df.iterrows():
        rec_time = row['recorded_at']
        if rec_time in existing_timestamps:
            continue

        temp_val = None
        if 'temperature' in row and pd.notna(row['temperature']):
            temp_val = Decimal(str(round(float(row['temperature']), 2)))
        elif 'Temperature' in row and pd.notna(row['Temperature']):
            temp_val = Decimal(str(round(float(row['Temperature']), 2)))

        records.append(ElectricityConsumption(
            user=user,
            recorded_at=rec_time,
            energy_kwh=Decimal(str(round(float(row['energy_kwh']), 3))),
            temperature=temp_val,
            source='dataset'
        ))

    if records:
        ElectricityConsumption.objects.bulk_create(records, batch_size=500)

    return len(records)

