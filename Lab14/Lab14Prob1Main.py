from expressMeal import ExpressMeal
from megaMeal import MegaMeal


def chooseMegaMeal():
    meal = MegaMeal()
    meal.chooseMeat()
    meal.chooseSide()
    meal.chooseDrink()
    meal.chooseDessert()
    meal.displayOrder()

def chooseExpressMeal():
    meal = ExpressMeal('','')
    meal.chooseMeat()
    meal.chooseSide()
    meal.displayOrder()

def main():
    mealChoice = int(input('Enter 1 for express meal or 2 for mega meal: '))

    if mealChoice == 1:
        chooseExpressMeal()
    elif mealChoice == 2:
        chooseMegaMeal()

main()
