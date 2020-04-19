import math
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
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
    def checkBinarySubtree(self, node, min, max):
            if (node.data > min) and (node.data<max):
                return node.data
            else: 
                raise Exception('This is not a binary tree.')
                
    def isBinarySearchTree(self, root, min = -math.inf, max = math.inf ):
        currentNode = root
        if (currentNode is not None):
            temp = self.checkBinarySubtree(currentNode, min, max)
            if (currentNode.left is not None):
                self.isBinarySearchTree(currentNode.left,min, temp)
            if (currentNode.right is not None):
                self.isBinarySearchTree(currentNode.right, temp, max)
        


root = Node(45)
myTree = BinaryTree(root)
root.left = Node(20)
root.right = Node(55)
root.left.left = Node(14)
root.left.right = Node(120)
root.right.left = Node(35)
root.right.right = Node(75)

myTree.isBinarySearchTree(root)
