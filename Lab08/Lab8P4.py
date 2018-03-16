def get_numbers():
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))

    return num_1,num_2

def large_small(_n1,_n2):

    if _n1 > _n2:
        large_num = _n1
        smal_num = _n2
    elif _n1 < _n2 or _n1 == _n2:
        large_num = _n2
        small_num = _n1

    return large_num, small_num

def main():
    _num1, _num2 = get_numbers()
    _largeNum, _smallNum = large_small(_num1, _num2)
    print("The larger number is: ", float(_largeNum))
    print("The smaller number is: ", float(_smallNum))

main()
