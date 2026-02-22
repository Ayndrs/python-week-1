from collections import defaultdict
from statistics import mean

def transform(patients):

    grouped = defaultdict(lambda: defaultdict(list))

    for patient in patients:
        grouped[patient.gender][patient.diabetes_risk_category].append(patient)

    summary = {}

    for gender, risk_groups in grouped.items():
        summary[gender] = {}

        for risk_category in ["Low Risk", "Prediabetes", "High Risk"]:
            group = risk_groups.get(risk_category, [])

            if not group:
                summary[gender][risk_category] = None
                continue

            summary[gender][risk_category] = {
                "count": len(group),
                "avg_bmi": mean(p.bmi for p in group),
                "avg_hba1c": mean(p.hba1c_level for p in group),
                "avg_glucose": mean(p.fasting_glucose_level for p in group),
                "avg_calorie_intake": mean(p.daily_calorie_intake for p in group),
                "avg_stress_level": mean(p.stress_level for p in group)
            }

    return summary