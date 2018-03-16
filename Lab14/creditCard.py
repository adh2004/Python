from card import Card


class CreditCard (Card):
    def __int__(self, cardNum, custName):
        super().__init__(cardNum, custName)
        self.__interest_rate = 0.0
        self.__credit_limit = 0

    def inputInfo(self, rate, limit):
        self.__interest_rate = rate
        self.__credit_limit = limit

    def  displayInfo(self):
        print('Interest rate: ' + str(self.__interest_rate) + ' Credit Limit: ' + str(self.__credit_limit))
