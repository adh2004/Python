class Customer:
        def __init__(self,custName):
            self.__Name = custName
            self.__credit_card_num = ""
            self.__debit_card_num = ""
            self.__debit_pin = ""
            self.__credit_security_code = ""

        def inputCardInfo(self):
            self.__credit_card_num = input('Enter credit card number: ')
            self.__credit_security_code = input('Enter 3-digit credit card security code: ')
            self.__debit_card_num = input('Enter 4-digit debit card number:')
            self.__debit_pin = input('Enter debit card pin: ')


        def verifyCredCard(self,security_Code):
            if security_Code == self.__credit_security_code:
                return True
            else:
                return False


        def verifyDebitCard(self,pin):
            if pin == self.__debit_pin:
                return True
            else:
                return False

        def creditCardLastFour(self):
            start_index = 11
            return_digits = 4
            ccFour = self.__credit_card_num[start_index:return_digits]
            return ccFour

        def debitCardLastFour(self):
            start_index = 11
            return_digits = 4
            dcFour = self.__debit_card_num[start_index:return_digits]
            return dcFour
