from pathlib import Path

fileName = 'workers.txt'
questions = {'Enter worker ID: ', 'Enter hourly rate: ', 'Enter number of work hours: '}

worker_profile = []
workers = 4
worker_file = open(fileName, 'w')
i = 0
complete_profile = []

while i <= 3:
    for q in questions:
        worker_profile.append(input(q))
    i += 1
x = 0
while x <= 11:
    for q in questions:
        worker_file.write(q + worker_profile[x])
        worker_file.write("\n")
        x += 1

worker_file.close()


worker_file = open(fileName, 'r')
for line in worker_file:
    print(line)

worker_file.close()
