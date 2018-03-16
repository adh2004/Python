

def calculate_bmi():
    height = float(input("Enter height(in inches): "))
    weight = float(input("Enter weight(in pounds): "))
    BMI = (703 * weight)/(height * height)
    print("Your BMI is: ", BMI)
    print()
    return


def hypertension():
    systolic_test = 140
    diastolic_test = 90

    systolic_input = int(input("Enter systolic pressure: "))
    diastolic_input = int(input("Enter diastolic pressure: "))

    if systolic_input >= systolic_test or diastolic_input >= diastolic_test:
        print("You have high blood pressure")
    else:
        print("Your blood pressure is normal")
    print()
    return


print("Health and Fitness Program")
print()
calculate_bmi()
hypertension()
