data = {
    'A': {'weight': 68, 'body_fat_percent': 20, 'activity_level': 'lightly active'},
    'B': {'weight': 92, 'body_fat_percent': 15, 'activity_level': 'very active'},
    'C': {'weight': 45, 'body_fat_percent': 35, 'activity_level': 'sedentary'},
    'D': {'weight': 76, 'body_fat_percent': 18, 'activity_level': 'moderately active'},
    'E': {'weight': 132, 'body_fat_percent': 42, 'activity_level': 'sedentary'}
}

################## คำนวณ BMR และ TDEE #########################

def calculate_bmr_from_lean_body_mass(weight, body_fat_percent):
    """
    คำนวณ BMR จาก Lean Body Mass (LBM)
    :param weight: น้ำหนัก (kg)
    :param body_fat_percent: ปริมาณไขมันในร่างกาย (%)
    :return: BMR (แคลอรี่)
    """
    lbm = weight * (1 - (body_fat_percent / 100))
    bmr = 370 + (21.6 * lbm)

    return bmr


def calculate_total_daily_energy_expenditure(bmr, activity_level):
    """
    คำนวณ Total Daily Energy Expenditure (TDEE) จาก BMR และ Activity Multiplier
    :param bmr: BMR (แคลอรี่)
    :param activity_level: Activity Multiplier (string)
    :return: TDEE (แคลอรี่)
    """
    if activity_level == 'sedentary':
        activity_multiplier = 1.2
    elif activity_level == 'lightly active':
        activity_multiplier = 1.375
    elif activity_level == 'moderately active':
        activity_multiplier = 1.55
    elif activity_level == 'very active':
        activity_multiplier = 1.725
    elif activity_level == 'extra active':
        activity_multiplier = 1.9
    else:
        raise ValueError("Activity level ไม่ถูกต้อง")

    tdee = bmr * activity_multiplier

    return tdee

######################################################################

for name, stats in data.items():
    weight = stats['weight']
    body_fat_percent = stats['body_fat_percent']
    activity_level = stats['activity_level']

    bmr = calculate_bmr_from_lean_body_mass(weight, body_fat_percent)
    tdee = calculate_total_daily_energy_expenditure(bmr, activity_level)

    print("{}: BMR = {:.2f}, TDEE = {:.2f}".format(name, bmr, tdee))