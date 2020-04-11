class BinaryHeap:
    def __init__(self, root=None):
        self.heap = []
        self.size = 0
    
    def insert(self,data):
        self.heap.append(data)
        self.size +=1
        self.heapifyUp()
    def get_min(self, root):
        if (self.size == 0 ):
            print("The heap is empty.")
        else:
            print("Min value is:", self.heapq[0])
            return self.heapq[0]
    def extract_min(self, root):
        if (self.size == 0 ):
            print("The heap is empty.")
        else:
            item = self.heapq[0]
            self.heapq[0]=self.heapq[self.size-1]
            self.size -=1
            self.heapifyDown();
            return item
    #Helpers
    #Magic formula:
        # from a node in level i
        # we can fin its children and parent using
        # left = i*2+1
        # right = i*2+2
        # parent = (i-2)/2
    def getLeftChildIndex(self, index):
            return index*2+1
    def getRightChildIndex(self, index):
            return index*2+2
    def getParentIndex(self, index):
            return int((index-2)/2)
            
    def hasLeftChild(self, index):
            return (index*2+1)<self.size
    def hasRightChild(self, index):
            return (index*2+2)<self.size
    def hasParent(self, index):
            return int((index-2)/2)>=0
            
    def getLeftChild(self, index):
            return self.heap[self.getLeftChildIndex(index)]
    def getRightChild(self, index):
            return self.heap[self.getRightChildIndex(index)]
    def getParent(self, index):
            return self.heap[self.getParentIndex(index)]  
            
    def swap (self, idx1, idx2):
        temp = self.heap[idx1]
        self.heap[idx1]=self.heap[idx2]
        self.heap[idx2]=temp
    def heapifyDown(self):
        pass
    def heapifyUp(self):
        index = self.size-1
        while ((self.hasParent(index))and(self.getParent(index)>self.heap[index])):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            #TODO

myHeap = BinaryHeap()
myHeap.insert(10)
myHeap.insert(15)
myHeap.insert(20)
myHeap.insert(17)
myHeap.insert(8)
