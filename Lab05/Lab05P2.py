passengerList = []
numOfPassengers = int(input("How many passengers in this flight?: "))
countedPassengers = 0
i = 0

def PrintList(*_list):
    print("This list:")
    for x in _list:
        print(x)

while countedPassengers <= (numOfPassengers -1):
    passengerName = input("Enter passenger Name: ")
    passengerList.append(passengerName)
    countedPassengers += 1

PrintList(passengerList)
passengerList.sort()
print("Passenger List after sort:", passengerList)
searchName = input("Enter a Name to search for: ")
for x in passengerList:
    if searchName == x:
        i +=1

if i == 0:
    print("This name is not found in passenger list")
removePassenger = input("Enter name of passenger to be removed: ")
passengerList.remove(removePassenger)
print("Passenger List after remove:",passengerList)
numOfPassengers -= 1
print("Number of passengers:",numOfPassengers)
