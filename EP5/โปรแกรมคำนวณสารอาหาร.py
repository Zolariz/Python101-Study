weight = float(input("น้ำหนักของคุณ (กิโลกรัม): "))
body_fat_percent = float(input("%ไขมันของคุณ: "))


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

activity_level = (input('ระดับกิจกรรมของคุณที่ทำในแต่ละสัปดาห์: '))
bmr = calculate_bmr_from_lean_body_mass(weight, body_fat_percent)
tdee = calculate_total_daily_energy_expenditure(bmr, activity_level)

print("BMR ของคุณ: {:.3f}".format(bmr))
print("TDEE ของคุณ: {:.3f}".format(tdee))


######################################################################

################### การวางสัดส่วนอาหาร ###################################

def calculate_macros_with_percentage(tdee, protein_percent, carbs_percent, fat_percent):
    """
    คำนวณสัดส่วนโปรตีน คาร์บ และไขมันในอาหารจากสัดส่วนเปอร์เซ็นต์
    :param tdee: Total Daily Energy Expenditure (แคลอรี่)
    :param protein_percent: สัดส่วนโปรตีนในอาหารเป็นเปอร์เซ็นต์
    :param carbs_percent: สัดส่วนคาร์บในอาหารเป็นเปอร์เซ็นต์
    :param fat_percent: สัดส่วนไขมันในอาหารเป็นเปอร์เซ็นต์
    :return: macros (tuple)
    """
    protein_calories = tdee * protein_percent / 100
    carbs_calories = tdee * carbs_percent / 100
    fat_calories = tdee * fat_percent / 100

    protein = protein_calories / 4
    carbs = carbs_calories / 4
    fat = fat_calories / 9

    meat = protein * 4.55
    rice = carbs * 3.4
    fats = fat / 13

    macros = (protein, carbs, fat)

    print(f"Protein: {protein:.2f} กรัม = เนื้อสัตว์ {round(meat, 2):.2f} กรัม")
    print(f"Carbs: {carbs:.2f} กรัม = ข้าว {round(rice, 2):.2f} กรัม")
    print(f"Fat: {fat:.2f} กรัม = น้ำมัน {round(fats, 2):.2f} ช้อน")

    return macros


tdee = calculate_total_daily_energy_expenditure(bmr, activity_level)
protein_percent = float(input('%Protein: '))
carbs_percent = float(input('%Carbs: '))
fat_percent = float(input('%Fat: '))

protein, carbs, fat = calculate_macros_with_percentage(tdee, protein_percent, carbs_percent, fat_percent)
