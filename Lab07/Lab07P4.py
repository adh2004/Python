def heart_rate_calculator(_age, _heartRate):
    target_heart_rate = (220 - _age - _heartRate) *0.4 + _heartRate
    print("Your target heart rate is: ",target_heart_rate)
def main():
    age = int(input("Enter age: "))
    restHeartRate = int(input("Enter resting heart rate: "))
    heart_rate_calculator(age, restHeartRate)

    return



main()
