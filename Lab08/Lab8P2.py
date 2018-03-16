def choose_room():
    single_room = 3000
    double_room = 2000
    print("Single room: $3000 per semester")
    print("Double room: $2000 per semester")
    sentinel = int(input("Enter 1 for single room, 2 for double room: "))

    if sentinel ==  1:
         cost = single_room
         print("Single room chosen")
    elif sentinel == 2:
        cost = double_room
        print("Double room chosen")
    else:
        cost = 0
    return cost


def choose_meal():
    meal_21 = 3500
    meal_15 = 2800
    print("21 - meal per week: $3500 per semester")
    print("15 - meal per week: $2800 per semester")
    sentinel = int(input("Enter 1 for 21-meal, 2 for 15-meal: "))

    if sentinel == 1:
        cost = meal_21
        print("21-meal chosen")
    elif sentinel == 2:
        cost = meal_15
        print("15-meal chosen")
    else:
        cost = 0
    return cost

def main():
    room_cost = choose_room()
    meal_cost = choose_meal()
    total_cost = room_cost + meal_cost

    print("Cost for room and board per semester: ",total_cost)

main()
