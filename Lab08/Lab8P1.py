def convert_to_euro(_usAmt):

    euro_amt = (_usAmt * 0.88)
    return euro_amt


def main():

    us_amt = float(input("Enter amount in US dollar: "))
    euro = convert_to_euro(us_amt)
    print("Equivalent amount in Euro: ",euro)

main()
