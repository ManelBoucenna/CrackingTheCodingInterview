# Compute complexity: O(n^2)
# Memory complexity: O(1)
def BubbleSort(arr):
    
    n = len(arr)
    for i in range(n):
        sorted = True
        for idx in range(0, n-i-1):
            if arr[idx +1] < arr[idx]:
                sorted = False
                arr[idx],arr[idx+1] = arr[idx+1],arr[idx]
        if sorted == True:
            break
    
    return arr

BubbleSort([4,5,2,8,1])
