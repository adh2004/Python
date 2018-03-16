roomLength = float(input('Enter room length: '))
while roomLength < 0:
    print('Room Length must be greater than 0')
    roomLength = float(input('Enter room length: '))
roomWidth = float(input('Enter room width: '))
while roomWidth < 0:
    print('Room Width must be greater than 0')
    roomWidth = float(input('Enter room length: '))
roomHeight = float(input('Enter room height: '))
while roomHeight < 0:
    print('Room Height must be greater than 0')
    roomHeight = float(input('Enter room height: '))
roomVolume = roomLength * roomWidth * roomHeight
btuNeeded = roomVolume * 3.5
print('BTU needed for this room:', btuNeeded)
