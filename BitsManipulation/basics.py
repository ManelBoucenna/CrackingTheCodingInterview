def GetBit(num, position):
    return (num & (1<<position))!=0

def SetBit(num, position):
    return num | (1<<position)

def ClearBit(num, position):
    mask = ~(1<<position)
    return num & mask

def ClearMSBtoPosition(num, position):# Clear from most significant bit to position
    #Ex: num = 11010, pos = 2 => num = 00010
    #    mask= 00011 = 11100 -1
    mask = (1<<position) -1 
    return num & mask

def ClearPositionToZero(num, position):
    #Ex: num = 11010, pos = 1 => num = 11000
    #    mask= 11100 = 1111<<2 = -1<<2
    mask = -1<<(position+1)
    return num & mask
    
def UpdateBit(num, pos, val):
    #Ex: num = 11010, pos = 1, val=0 => num = 11000
    #    mask= 11101 = ~00010
    value = 1 if val else 0
    mask = ~(1<<pos)
    return (num  & mask)|(val<<pos)
    
UpdateBit(8,0,True)
