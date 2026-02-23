"""This is a module that extracts from a csv file"""
import csv
from models import PatientRecord

def extract(file_path: str) -> list[PatientRecord]:
    """This function extracts data from a csv file"""
    records = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            record = PatientRecord(
                patient_id=row["Patient_ID"],
                age=int(row["age"]),
                gender=row["gender"],
                bmi=float(row["bmi"]),
                blood_pressure=float(row["blood_pressure"]),
                fasting_glucose_level=float(row["fasting_glucose_level"]),
                insulin_level=float(row["insulin_level"]),
                hba1c_level=float(row["HbA1c_level"]),
                cholesterol_level=float(row["cholesterol_level"]),
                triglycerides_level=float(row["triglycerides_level"]),
                physical_activity_level=str(row["physical_activity_level"]),
                daily_calorie_intake=int(row["daily_calorie_intake"]),
                sugar_intake_grams_per_day=float(row["sugar_intake_grams_per_day"]),
                sleep_hours=float(row["sleep_hours"]),
                stress_level=int(row["stress_level"]),
                family_history_diabetes=row["family_history_diabetes"] == "1",
                waist_circumference_cm=float(row["waist_circumference_cm"]),
                diabetes_risk_score=float(row["diabetes_risk_score"]),
                diabetes_risk_category=row["diabetes_risk_category"]
            )

            records.append(record)
    return records
