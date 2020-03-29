class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
        self.size = 1
    def Append(self, data):
        newNode = Node(data)
        if (self.headval == None):
            self.headval = newNode
            return
        currentNode = self.headval
        while currentNode.nextval is not None:
            currentNode = currentNode.nextval
        currentNode.nextval = newNode
        self.size += 1
    def LoopDetection(self):
        # Check if there's a loop
        # Find where the loop starts

List = SLinkedList()

List.Append(1)
List.Append(2)
List.Append(3)
List.Append(2)
List.Append(3)

List.LoopDetection()
