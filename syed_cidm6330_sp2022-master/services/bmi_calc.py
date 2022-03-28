import bisect
from datetime import date

def bmi_score(height: float, weight: float, gender, age: int) -> float:
    # always provide credit for the source of any calculation
    # https://stackoverflow.com/questions/48857564/
    bmi = round(weight / ((height/100) ** 2))
    return bmi

def age(date_of_birth):
    #https://www.codingem.com/how-to-calculate-age-in-python/
    today = date.today()
    one_or_zero = ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    year_difference = today.year - date_of_birth.year
    age = year_difference - one_or_zero
    
    return age

def bmi_category(date_of_birth, age, bmi_score, optimal_bmi_range_min_ages, optimal_bmi_ranges, optimal_bmi_range, bmi_categories, bmi_cat_thresholds):

    if age < 19:
        print("You're too young for this and I'm concerned you may be at risk of developing an eating disorder.")
        exit()

    optimal_bmi_range_min_ages = [25, 35, 45, 55, 65]
    optimal_bmi_ranges = [(19, 24), (20, 25), (21, 26), (22, 27), (23, 28), (24, 29)]
    optimal_bmi_range = optimal_bmi_ranges[bisect.bisect_left(optimal_bmi_range_min_ages, age)]

    if bmi >= optimal_bmi_range[0] and bmi <= optimal_bmi_range[1]:
        print("Your BMI is optimal for your age!")
    else:
        print("Your BMI is not okay for your age!!!")

    bmi_categories = ["underweight", "normal weight", "overweight", "obesity", "strong obesity"]
    if gender == "m":
        bmi_cat_thresholds = [20, 26, 31, 41]
    elif gender == "f":
        bmi_cat_thresholds = [19, 25, 31, 41]
    else:
        print("Your BMI is",bmi)
        exit()

def bmi_evaluation(bmi_category):
    bmi_category = bmi_categories[bisect.bisect_left(bmi_cat_thresholds,bmi)]
    print("Your BMI is " + str(bmi) + ". That means " + bmi_category)