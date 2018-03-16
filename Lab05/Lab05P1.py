list = [4,1,7,6]

def PrintList(*_list):
    print("This list:")
    for x in _list:
        print(x)

PrintList(list)
list[1]=2
PrintList(list)
list[-1]=5
PrintList(list)
list.append(8)
PrintList(list)
list.insert(0,9)
PrintList(list)
