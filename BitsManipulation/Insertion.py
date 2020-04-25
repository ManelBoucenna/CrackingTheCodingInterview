def Insertion(N, M, i, j):
    # Case:
    #N = 10000000000, M = 10011, i =2, j=6
    # Result = 1000(10011)00 = 556
    # Mask = 1111000011 = ~0000111100 = ~(1111<<i)

    left_mask = -1<<j
    right_mask = ~(-1<<i)
    mask = left_mask | right_mask
    return (N & mask)|(M<<i)


Insertion(1024, 19, 2, 6)
