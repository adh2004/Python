_tuple = (7,5,2,8)
_list = list(_tuple)
_list[2] = 1
_tuple = tuple(_list)
print("Tuple after element change: ",_tuple)
