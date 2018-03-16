intToCount = 6
int_count = 1
smallint_list = []
bigint_list = []

while int_count <= intToCount:
    smallint_list.append(int((input("Enter an integer: "))))
    int_count +=1
print("This list: ",smallint_list)

for x in smallint_list:
    if x > 20:
        bigint_list.append(x)

print("List of integers greater than 20:",bigint_list)
