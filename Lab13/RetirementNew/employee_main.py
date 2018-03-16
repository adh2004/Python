from employee import Employee
def main():
    emp_name1 = ''
    emp_salary1 = 0
    emp_year1 = 0
    sentinel = 0

    emp_name1 = input('Enter name: ')
    emp_salary1 = float(input('Enter salary: '))
    emp_year1 = float(input('Enter years of service: '))

    employee1 = Employee(emp_name1, emp_salary1, emp_year1)
    print(employee1.__str__())
    print('')

    while sentinel != 3:
        sentinel = int(input('Enter 1 to change salary, 2 to change years of service, 3 to exit: '))

        if sentinel == 1:
            salary = float(input('Enter new salary: '))
            employee1.setSalary(salary)
        elif sentinel == 2:
            years = float(input('Enter new years of service: '))
            employee1.setYears(years)

    print(employee1.__str__())
    print('Monthly pension payout: ',employee1.pension())
main()
