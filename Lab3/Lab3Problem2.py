roomLength = float(input('Enter room length: '))
roomWidth = float(input('Enter room width: '))
roomHeight = float(input('Enter room height: '))
sunlight = input('Does the room get a lot of sunlight? [yes/no] ')
roomVolume = roomLength * roomWidth * roomHeight
calcConstant = 3.5
increasePercent = .20
BTU = roomVolume * calcConstant

if sunlight == 'yes':
    BTUNew = BTU + (BTU * increasePercent)
    print('BTU needed for the air conditioner: ', BTUNew)
else:
    print('BTU needed for the air conditioner: ',BTU)
