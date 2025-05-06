def main():
    print("===============================================")
    print("      ADVANCED MEDICAL EXPERT SYSTEM - v3.0")
    print(" Focus Areas: Diabetes, Hypertension, General Risk")
    print("===============================================\n")

    # Getting basic and medical inputs
    age = int(input("Enter your age: ").strip())
    weight = float(input("Enter your weight (in kg): ").strip())

    # Sugar levels
    fasting_sugar = float(input("Enter fasting blood sugar level (mg/dL): ").strip())
    post_meal_sugar = float(input("Enter post-meal blood sugar level (mg/dL): ").strip())

    # Blood pressure
    systolic_bp = int(input("Enter systolic BP (upper number): ").strip())
    diastolic_bp = int(input("Enter diastolic BP (lower number): ").strip())

    # Symptoms and history
    history_diabetes = input("Do you have a history of diabetes? (yes/no): ").strip().lower()
    frequent_thirst = input("Do you often feel thirsty? (yes/no): ").strip().lower()
    frequent_urination = input("Do you urinate frequently? (yes/no): ").strip().lower()
    blurred_vision = input("Do you have blurred vision? (yes/no): ").strip().lower()
    fatigue = input("Do you feel tired often? (yes/no): ").strip().lower()
    chest_pain = input("Do you experience chest pain? (yes/no): ").strip().lower()
    headache = input("Do you experience frequent headaches? (yes/no): ").strip().lower()

    print("\n======= DIAGNOSIS REPORT =======\n")

    # Flags to track conditions
    diabetes_risk = False
    hypertension_risk = False
    mild_warning = False

    # -----------------------------------------
    # Diabetes Evaluation
    # -----------------------------------------
    if fasting_sugar >= 126 and post_meal_sugar >= 200:
        diabetes_risk = True
        print(" Diagnosis: You are likely diabetic.")
        if history_diabetes == 'yes':
            print("  Note: Previous history of diabetes detected. Blood sugar levels are dangerously high.")
        else:
            print(" Warning: Blood sugar values indicate diabetes without known history.")
        print(" Suggestion: Consult a diabetologist. Start sugar control medications and monitor diet.\n")

    elif 100 <= fasting_sugar < 126 or 140 <= post_meal_sugar < 200:
        diabetes_risk = True
        print(" Diagnosis: You are in a pre-diabetic stage.")
        print(" Suggestion: Exercise, maintain diet, monitor levels monthly. Reverse possible with care.\n")

    elif (frequent_thirst == 'yes' or frequent_urination == 'yes' or 
          blurred_vision == 'yes' or fatigue == 'yes') and (fasting_sugar > 110 or post_meal_sugar > 160):
        diabetes_risk = True
        print(" Diagnosis: Symptoms and borderline sugar levels suggest early diabetes.")
        print(" Suggestion: Take HbA1c test. Meet a physician for preemptive treatment.\n")

    else:
        print("Blood sugar levels are within safe range.\n")

    # -----------------------------------------
    # Hypertension Evaluation
    # -----------------------------------------
    if systolic_bp >= 140 or diastolic_bp >= 90:
        hypertension_risk = True
        print(" Diagnosis: You have Hypertension (High Blood Pressure).")
        if chest_pain == 'yes':
            print(" Chest pain reported. Immediate attention recommended.")
        if headache == 'yes':
            print(" Frequent headaches may indicate vascular stress.")
        print(" Suggestion: Reduce salt intake, check BP regularly, consult cardiologist.\n")

    elif 120 <= systolic_bp < 140 or 80 <= diastolic_bp < 90:
        hypertension_risk = True
        print(" Diagnosis: Pre-hypertension detected.")
        print(" Suggestion: Lifestyle management needed. Monitor regularly to prevent progression.\n")

    else:
        print(" Blood pressure is within normal range.\n")

    # -----------------------------------------
    # General Symptom Checks (with no risk detected above)
    # -----------------------------------------
    if not diabetes_risk and not hypertension_risk:
        if (frequent_thirst == 'yes' or frequent_urination == 'yes' or 
            blurred_vision == 'yes' or fatigue == 'yes'):
            mild_warning = True
            print("  Warning: Some symptoms detected even though medical levels are normal.")
            print(" Suggestion: Repeat tests in 2 weeks. Avoid sugar/starch. Track your symptoms.\n")

        if chest_pain == 'yes' or headache == 'yes':
            mild_warning = True
            print("  Chest pain/headache detected without high BP.")
            print(" Suggestion: Could be stress-related. Consider ECG or physician consultation.\n")

    # -----------------------------------------
    # Final Summary
    # -----------------------------------------
    if not diabetes_risk and not hypertension_risk and not mild_warning:
        print(" You are in good health based on all provided data.")
        if age > 45:
            print(" Recommendation: Periodic checkups are still advised due to age group.\n")
        else:
            print(" Keep exercising and eating healthy!\n")

    print("======= END OF REPORT =======")

# Run system
if __name__ == "__main__":
    main()
