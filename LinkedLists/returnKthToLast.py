class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
    def Append(self, data):
        newNode = Node(data)
        if (self.headval == None):
            self.headval = newNode
            return
        currentNode = self.headval
        while currentNode.nextval is not None:
            currentNode = currentNode.nextval
        currentNode.nextval = newNode
        
    def KthToLast1(self,k):# Compute size then repass to find item's position O(2*n)
        size = 0
        currentNode = self.headval
        while currentNode is not None:
            size +=1
            currentNode = currentNode.nextval
        currentNode = self.headval
        position = 1
        while currentNode is not None:
            if (position == (size - k)):
                print("The value is:", currentNode.dataval)
                return
            position += 1
            currentNode = currentNode.nextval
            
    def KthToLast2(self,k):# O(n)
        
        pointerFast = self.headval
        pointerSlow = self.headval
        for i in range(k):
            pointerFast = pointerFast.nextval

        while pointerFast.nextval is not None:
            pointerFast = pointerFast.nextval
            pointerSlow = pointerSlow.nextval
        print("The value is:", pointerSlow.dataval)
            

myList = SLinkedList()
myList.headval = Node(3)
myList.Append(1)
myList.Append(2)
myList.Append(1)
myList.Append(2)
myList.Append(3)

#myList.KthToLast1(1)
myList.KthToLast2(1)
