
count_soldHouses = int(input("How many houses are sold? "))
iteration_List = range(0,count_soldHouses,1)
house_price = []
commission_percent = .03
commission = []


for i in iteration_List:
    house_price.append(int(input("Enter price of a house: ")))

for i in iteration_List:
    commission.append(commission_percent * house_price[i])
    print("House price: ",house_price[i]," Commission: ",commission[i])






