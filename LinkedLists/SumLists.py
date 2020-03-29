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
        
def SumListsReversed(headvalA, headvalB):# O(n)
    rest = 0
    total = 0
    newList = SLinkedList()
    currentNodeA = headvalA
    currentNodeB = headvalB
    while (currentNodeA is not None) and (currentNodeB is not None):
        total = currentNodeA.dataval + currentNodeB.dataval + rest
        rest = total // 10
        newList.Append(total%10)
        currentNodeA = currentNodeA.nextval
        currentNodeB = currentNodeB.nextval
    if (currentNodeA is None) and (currentNodeB is not None):
        while (currentNodeB is not None):
            total = currentNodeB.dataval + rest
            rest = total // 10
            newList.Append(total%10)
            currentNodeB = currentNodeB.nextval
    elif (currentNodeB is None) and (currentNodeA is not None):
        while (currentNodeA is not None):
                    total = currentNodeA.dataval + rest
                    rest = total // 10
                    newList.Append(total%10)
                    currentNodeA = currentNodeA.nextval
    if (rest > 0 ):
        newList.Append(rest)
    return newList

def SumListsNotReversed(headvalA, headvalB, sizeA, sizeB):# 
    pass
    
ListA = SLinkedList()
ListB = SLinkedList()

ListA.Append(9)
ListA.Append(7)
ListA.Append(8)

ListB.Append(6)
ListB.Append(8)
ListB.Append(5)

SumList = SumListsNotReversed(ListA.headval, ListB.headval, sizeA, sizeB)
