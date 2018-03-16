class Card:

    def __init__(self, cardNumber, customerName):
        self.__id = cardNumber
        self.__name = customerName

    def displayIdName(self):
        print('Id: ', self.__id, ' Name: ', self.__name)

    def inputInfo(self):
        raise NotImplementedError

    def displayInfo(self):
        raise NotImplementedError
