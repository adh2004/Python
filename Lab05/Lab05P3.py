sentinel = 'y'
uSentinel = sentinel.upper()
flightCount = 0
lFlightMilage = []

def AddMilage(_list):
    milageTotal = 0
    for x in _list:
        milageTotal += x
    print("Total milage so far: ", milageTotal)

def PrintFlightMiles(_list):
    print("Milage of each flight you have taken:")
    for x in _list:
        print(x)

while uSentinel == 'Y':
    lFlightMilage.append(int(input("Enter milage of a flight: ")))
    flightCount += 1
    print("Number of flights so far: ",flightCount)
    AddMilage(lFlightMilage)
    sentinel = input("Enter another flight? [y/n] ",)
    uSentinel = sentinel.upper()
    if uSentinel == 'N':
        PrintFlightMiles(lFlightMilage)
