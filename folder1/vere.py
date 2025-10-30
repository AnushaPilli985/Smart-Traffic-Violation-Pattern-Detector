from datetime import datetime, timedelta

def calculate_due_date(lmp_date):
    return lmp_date + timedelta(days=280)  # 40 weeks from LMP

def calculate_trimester(weeks):
    if weeks < 13:
        return "First Trimester"
    elif 13 <= weeks < 28:
        return "Second Trimester"
    else:
        return "Third Trimester"

def weight_analysis(pre_preg_weight, current_weight, weeks):
    weight_gain = current_weight - pre_preg_weight
    # Rough guideline based on normal BMI
    if weeks < 13:
        ideal_gain = 0.5 - 2
    elif weeks < 28:
        ideal_gain = 5 - 6.5
    else:
        ideal_gain = 11 - 16

    print(f"Total weight gain so far: {weight_gain:.1f} kg")
    if weight_gain < ideal_gain[0]:
        print("Warning: Weight gain is below the recommended range.")
    elif weight_gain > ideal_gain[1]:
        print("Warning: Weight gain is above the recommended range.")
    else:
        print("Weight gain is within the recommended range.")

# ----------- Input Section -----------

lmp_input = input("Enter your Last Menstrual Period (YYYY-MM-DD): ")
lmp_date = datetime.strptime(lmp_input, "%Y-%m-%d")
today = datetime.today()

weeks_pregnant = (today - lmp_date).days // 7
due_date = calculate_due_date(lmp_date)

print(f"\nEstimated Due Date: {due_date.strftime('%Y-%m-%d')}")
print(f"Weeks Pregnant: {weeks_pregnant}")
print(f"Trimester: {calculate_trimester(weeks_pregnant)}")

# Optional: Weight Analysis
pre_weight = float(input("Enter your pre-pregnancy weight (kg): "))
current_weight = float(input("Enter your current weight (kg): "))

weight_analysis(pre_weight, current_weight, weeks_pregnant)