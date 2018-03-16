residence = input('Enter R for residential or B for business: ')
resType = residence.capitalize()
gallonsUsed = float(input('How many gallons of water were used? '))
busCharge = 0.005
busOverCharge = 0.009
resCharge = 0.004
resOverCharge = 0.007
busGalNormal = 10000
resGalNormal = 8000

if resType == 'R':
    payAmount = resGalNormal * resCharge
    if gallonsUsed > resGalNormal:
        galDifference = gallonsUsed - resGalNormal
        payAmount = payAmount + (galDifference * resOverCharge)
        if gallonsUsed <= resGalNormal:
            payAmount = gallonsUsed * resCharge

else:
    payAmount = busGalNormal * busCharge
    if gallonsUsed > busGalNormal:
        galDifference = gallonsUsed - busGalNormal
        payAmount = payAmount + (galDifference * busOverCharge)
        if gallonsUsed <= busGalNormal:
            payAmount = gallonsUsed * busCharge

print('Please pay this amount ', payAmount)



