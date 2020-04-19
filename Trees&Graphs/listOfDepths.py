class Linked_Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        
    def append(self, newdata):
        NewNode = Linked_Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode     
        
        
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.linkedListsPerLevel = dict()
        
    def insert(self,data, root = None):
        if (root is None):
            root = self.root
        currentNode = root
        if (data<currentNode.data):
            if (currentNode.left is None):
                currentNode.left = Node(data)
            else:
                self.insert(data,currentNode.left)
        else:
            if (currentNode.right is None):
                currentNode.right = Node(data)
            else:
                self.insert(data,currentNode.right)
    def listOfDepth(self,root,depth = 0):
        currentNode = root       
        
        if (currentNode is not None):
            self.MakeListAtDepth(depth, currentNode.data)
            depth+=1
            self.listOfDepth(currentNode.left,depth)
            self.listOfDepth(currentNode.right,depth)
        
        return self.linkedListsPerLevel
        
    def MakeListAtDepth(self, depth, data):
        if (depth in self.linkedListsPerLevel):
            self.linkedListsPerLevel[depth].append(data)
        else:
            self.linkedListsPerLevel[depth]=SLinkedList()
            self.linkedListsPerLevel[depth].append(data)
    def isTreeEmpty(self):
        if (self.root is None):
            return True
        else:
            return False

root = Node(45)
myTree = BinaryTree(root)
myTree.insert(25)
myTree.insert(75)
myTree.insert(15)
myTree.insert(35)
myTree.listOfDepth(root)
