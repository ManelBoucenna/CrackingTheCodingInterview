def convert(numA, numB):
    #Case:
    # numA = 11101
    # num B = 01111
    # return 2
    difference = 0

    while ((numA is not 0) or (numB is not 0)):
        difference += GetBit(numA, 0) ^ GetBit(numB, 0)
        numA >>=1
        numB >>=1
    return difference
    
def GetBit(num, position):
    return 1 if (num & (1<<position))!=0 else 0
    
convert(29,15)
