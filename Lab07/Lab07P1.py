

def calculate_bmi():
    height = float(input("Enter height(in inches): "))
    weight = float(input("Enter weight(in pounds): "))
    BMI = (703 * weight)/(height * height)
    print("Your BMI is: ", BMI)
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
    return


print("Health and Fitness Program")
print()
print("Enter 1 to calculate BMI only")
print("Enter 2 to check if you have high blood pressure only")
print("Enter 3 to do both")
choice = int(input("Enter your choice: "))
if choice == 1:
    calculate_bmi()
elif choice == 2:
    hypertension()
elif choice == 3:
    calculate_bmi()
    hypertension()
else:
    print("Please enter a valid choice")
    choice = int(input("Enter your choice: "))
