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
        
    def DeleteMiddleNode(self,node):#O(1)
        node.dataval = node.nextval.dataval
        node.nextval = node.nextval.nextval

myList = SLinkedList()
myList.headval = Node("a")
myList.Append("b")
myList.Append("c")
myList.Append("d")

node = myList.headval.nextval.nextval
myList.DeleteMiddleNode(node)
