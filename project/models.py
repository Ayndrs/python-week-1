from dataclasses import dataclass

@dataclass
class PatientRecord:
    patient_id: str
    age: int
    gender: str
    bmi: float
    blood_pressure: float
    fasting_glucose_level: float
    insulin_level: float
    hba1c_level: float
    cholesterol_level: float
    triglycerides_level: float
    physical_activity_level: str
    daily_calorie_intake: int
    sugar_intake_grams_per_day: float
    sleep_hours: float
    stress_level: int
    family_history_diabetes: bool
    waist_circumference_cm: float
    diabetes_risk_score: float
    diabetes_risk_category: str