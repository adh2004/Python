from expressMeal import ExpressMeal


class MegaMeal(ExpressMeal):
    def __init__(self):
        super().__init__('','')
        self._drink = ''
        self._dessert = ''

    def chooseDrink(self):
        drinkChoice = int(input('Enter 1 for soda or 2 for iced tea: '))

        if drinkChoice == 1:
            self._drink = 'soda'
        elif drinkChoice == 2:
            self._drink == 'iced tea'

    def chooseDessert(self):
        dessertChoice = int(input('Enter 1 for ice-cream or 2 for cookie: '))

        if dessertChoice == 1:
            self._dessert = 'ice-cream'
        elif dessertChoice == 2:
            self._dessert = 'cookie'

    def displayOrder(self):
        if self._meat == '' and self._side != '' and self._drink != '' and self._dessert != '':
            print('Items ordered: No meat ordered', self._side, 'and', self._drink, 'and', self._dessert)
        elif self._meat != '' and self._side == '' and self._drink != '' and self._dessert != '':
            print('Items ordered: ',self._meat, 'No side ordered', 'and',self._drink, 'and',self._dessert)
        elif self._meat != '' and self._side != '' and self._drink == '' and self._dessert != '':
            print('Items ordered: ',self._meat, 'and', self._side , 'No drink ordered', 'and',self._dessert)
        elif self._meat != '' and self._side != '' and self._drink != '' and self._dessert == '':
            print('Items ordered: ',self._meat, 'and',self._side ,'and', self._drink, 'No dessert ordered')
        elif self._meat == '' and self._side == '' and self._drink == '' and self._dessert == '':
            print('No items ordered')
        else:
            print('Items ordered: ', self._meat, 'and', self._side, 'and', self._drink,'and', self._dessert)
