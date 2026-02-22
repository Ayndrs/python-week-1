def load(summary):

    for gender, risk_groups in summary.items():
        print("\n============================")
        print(f"{gender.upper()} PATIENT ANALYSIS")
        print("============================")

        for risk_category, metrics in risk_groups.items():
            print(f"\n{risk_category}:")

            if metrics is None:
                print("  No data available")
                continue

            print(f"  Count: {metrics['count']}")
            print(f"  Avg BMI: {metrics['avg_bmi']:.2f}")
            print(f"  Avg HbA1c: {metrics['avg_hba1c']:.2f}")
            print(f"  Avg Fasting Glucose: {metrics['avg_glucose']:.2f}")
            print(f"  Avg Daily Calorie Intake: {metrics['avg_calorie_intake']:.2f}")
            print(f"  Avg Stress Level: {metrics['avg_stress_level']:.2f}")