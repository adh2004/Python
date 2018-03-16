def Tuition_instate(_creditHrs):
    creditHrCost = 60
    print("You are paying in-state")
    if _creditHrs <= 12:
        cost = _creditHrs * creditHrCost
    else:
        cost = creditHrCost * 12
    print("Please pay: $", cost)


def Tuition__outstate(_creditHrs):
    creditHrCost = 200
    print("You are paying out-of-state")
    if _creditHrs <= 15:
        cost = _creditHrs * creditHrCost
    else:
        cost = creditHrCost * 15
    print("Please pay: $", cost)

sentinel = str(input("Are you in-state students? [y/n]: "))
uSentinel = sentinel.upper()
creditHours = int(input("How many credit hours are you taking? "))

if uSentinel == 'Y':
    Tuition_instate(creditHours)
else:
    Tuition__outstate(creditHours)

