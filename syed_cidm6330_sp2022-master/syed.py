class health_record:
    height = float(input('Please enter in your height in inches:' ))
    weight = float(input('Please enter in your weight in pounds:' ))
    gender = input('Please enter in your gender (M or F):' )
    dob = input('Please enter in your date of birth (MM/DD/YYYY)')
    def bmi_calc(height, weight):
        bmi = weight/(height**2) * 703
        if (bmi < 16):
            return 'extremely underweight', bmi
        elif (bmi >= 16 and bmi < 18.5):
            return 'underweight', bmi
        elif (bmi >= 18.5 and bmi < 25):
            return 'healthy', bmi
        elif (bmi >= 25 and bmi < 30):
            return 'overweight', bmi
        elif (bmi >= 30):
            return 'obese', bmi

    quote, bmi = bmi_calc(height, weight)
    print('Your BMI is: {} and you are: {}'.format(bmi, quote))