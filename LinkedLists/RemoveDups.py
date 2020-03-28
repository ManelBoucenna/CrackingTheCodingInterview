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
    def RemoveDupsWithoutBuffer(self):#O(n^2)
        if (self.headval == None):
            print("This list is empty.")
            return
        
        previousNode2 = None
        currentNode1 = self.headval
        currentNode2 = currentNode1.nextval
        
        while currentNode1 is not None:
            previousNode2 = currentNode1
            currentNode2 = currentNode1.nextval
            
            while currentNode2 is not None:
                if (currentNode2.dataval == currentNode1.dataval):
                    #Remove Node 2
                    if (currentNode2.nextval is None):
                        previousNode2.nextval = None
                    else:
                        previousNode2.nextval = currentNode2.nextval
                else:
                    previousNode2 = currentNode2
                currentNode2 = previousNode2.nextval
            currentNode1 = currentNode1.nextval  
            
    def RemoveDupsWithBuffer(self): #O(n)
        if (self.headval == None):
            print("This list is empty.")
            return
        
        previousNode = None
        currentNode = self.headval
        dict_vals = dict()
        
        while (currentNode is not None):
            if (currentNode.dataval in dict_vals):
                #remove node
                if (currentNode.nextval is None):
                    previousNode.nextval = None
                else:
                    previousNode.nextval = currentNode.nextval
            else:
                dict_vals[currentNode.dataval] = 1
                previousNode = currentNode
            currentNode = previousNode.nextval
            

myList = SLinkedList()
myList.headval = Node(3)
myList.Append(1)
myList.Append(2)
myList.Append(1)
myList.Append(2)
myList.Append(3)

myList.RemoveDupsWithoutBuffer()
#myList.RemoveDupsWithBuffer()
