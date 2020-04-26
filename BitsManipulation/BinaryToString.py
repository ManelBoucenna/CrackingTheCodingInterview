def BinaryToString(num):
    # Case:
    #num = 0.75 =0.11
    bit_printed = 1
    bits = ["."]
    while(num>0):
        r = num*2
        if (r>=1):
            bits.append("1")
            num = r - 1
        else:
            bits.append("0")
            num = r
        if (bit_printed>31):
            return ("Error!")
        bit_printed +=1
    print(bits)

BinaryToString(0.96)
