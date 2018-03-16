def choose_room():
    single_room = 3000
    double_room = 2000
    print("Single room: $3000 per semester")
    print("Double room: $2000 per semester")
    sentinel = int(input("Enter 1 for single room, 2 for double room: "))

    if sentinel ==  1:
         print("Single room chosen")
         return single_room
    elif sentinel == 2:
        print("Double room chosen")
        return double_room

def choose_meal():
    meal_21 = 3500
    meal_15 = 2800
    print("21 - meal per week: $3500 per semester")
    print("15 - meal per week: $2800 per semester")
    sentinel = int(input("Enter 1 for 21-meal, 2 for 15-meal: "))

    if sentinel == 1:
        print("21-meal chosen")
        return  meal_21
    elif sentinel == 2:
        print("15-meal chosen")
        return meal_15


def main():
    room_cost = choose_room()
    meal_cost = choose_meal()
    total_cost = room_cost + meal_cost

    print("Cost for room and board per semester: ",total_cost)

main()
