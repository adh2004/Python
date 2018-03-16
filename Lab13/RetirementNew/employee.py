class Employee:
    def __init__(self, e_Name, e_Salary, e_Years):
        self.__name = e_Name
        self.__salary = e_Salary
        self.__years = e_Years

    def pension(self):
        _pensionPay = (self.__salary * self.__years)* 0.0015
        return _pensionPay
    def setSalary(self, Salary):
        self.__salary = Salary

    def setYears(self, Years):
        self.__years = Years

    def __str__(self):
        return 'Name: ' + self.__name + ' Salary: '+ str(self.__salary) + ' Years of service: ' + str(self.__years)
