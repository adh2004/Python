class Employee:
    def __init__(self, e_Name, e_Salary, e_Years):
        self.name = e_Name
        self.salary = e_Salary
        self.years = e_Years

    def pension(self):
        _pensionPay = (self.salary * self.years)* 0.0015
        return _pensionPay
