from card import Card


class DebitCard(Card):
    def __init__(self, cardNum, custName):
            super().__init__(cardNum, custName)
            self.__pin = 0000
            self.__fund_available = 0.0

    def inputInfo(self, pinCode, fundAvailable):
        self.__pin = pinCode
        self.__fund_available = fundAvailable

    def displayInfo(self):
        print('Pin: ' + str(self.__pin) + ' Fund Available: ' + str(self.__fund_available))
