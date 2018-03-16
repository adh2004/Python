class ExpressMeal:

    def __init__(self, meat, side):
        self._meat = ''
        self._side = ''

    def chooseMeat(self):
        meatChoice = int(input('Enter 1 for chicken sandwich or 2 for cheese burger: '))

        if meatChoice == 1:
            self._meat = 'chicken sandwich'
        elif meatChoice == 2:
            self._meat = 'cheese burger'


    def chooseSide(self):
        sideChoice = int(input('Enter 1 for fries or 2 for chips: '))

        if sideChoice == 1:
            self._side = 'fries'
        elif sideChoice == 2:
            self._side = 'chips'

    def displayOrder(self):
        if self._meat == '' and self._side != '':
            print('Items ordered: No meat ordered', self._side)
        elif self._meat != '' and self._side == '':
            print('Items ordered: ',self._meat, 'No side ordered')
        elif self._meat == '' and self._side == '':
            print('No items ordered')
        else:
            print('Items ordered: ', self._meat, 'and' ,self._side)
