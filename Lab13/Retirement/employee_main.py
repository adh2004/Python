from employee import Employee
def main():
    emp_name1 = ''
    emp_salary1 = 0
    emp_year1 = 0
    emp_name2 = ''
    emp_salary2 = 0
    emp_years2 = 0

    emp_name1 = input('Enter name: ')
    emp_salary1 = float(input('Enter salary: '))
    emp_year1 = float(input('Enter years of service: '))

    employee1 = Employee(emp_name1, emp_salary1, emp_year1)
    print('Monthly pension payout: ',employee1.pension())
    print('')

    emp_name2 = input('Enter name: ')
    emp_salary2 = float(input('Enter salary: '))
    emp_year2 = float(input('Enter years of service: '))

    employee2 = Employee(emp_name2, emp_salary2, emp_year2)
    print('Monthly pension payout: ',employee2.pension())

main()
