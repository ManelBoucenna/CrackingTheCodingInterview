class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def printList(self):
        if (self.headval == None):
            print("This list is empty.")
            return
        currentNode = self.headval
        while currentNode is not None:
            print (currentNode.dataval)
            currentNode = currentNode.nextval
            
    def Prepend(self, data):
        newNode = Node(data)
        if (self.headval == None):
            self.headval = newNode
            return
        newNode.nextval = self.headval
        self.headval = newNode
    def Append(self, data):
        newNode = Node(data)
        if (self.headval == None):
            self.headval = newNode
            return
        currentNode = self.headval
        while currentNode.nextval is not None:
            currentNode = currentNode.nextval
        currentNode.nextval = newNode
    def Remove(self, data):
        if (self.headval == None):
            print("This list is empty.")
            return
        currentNode = self.headval
        while currentNode is not None:
            if currentNode.nextval.dataval == data:
                if currentNode.nextval.nextval is not None:
                    currentNode.nextval = currentNode.nextval.nextval
                else:
                    currentNode.nextval = None
                return
            currentNode = currentNode.nextval
        print('Element Not found')
            
myList = SLinkedList()
myList.headval = Node("1")
myList.Prepend("0")
myList.Append("2")
myList.Remove("1")

myList.printList()
