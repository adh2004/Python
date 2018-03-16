worker_file = open('workers.txt','r')
str = []
Rate = 0
Hours = 0
current_ID = 0
for line in worker_file:
    str = line.split(':', 1)
    if str[0] == 'Enter worker ID':
        ID = int(str[1])
    elif str[0] == 'Enter hourly rate':
        Rate = float(str[1])
    else:
        Hours = float(str[1])

    if ID > current_ID and Hours > 0:
        gross_pay = Rate * Hours
        print('ID: ', ID, 'Gross Pay: ', gross_pay)
        current_ID = ID
        Hours = 0
worker_file.close()


