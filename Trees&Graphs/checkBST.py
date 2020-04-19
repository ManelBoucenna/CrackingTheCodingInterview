import math
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.isBST = True
        
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
        if (node.data>min) and (node.data<max):  
            if (node.left is not None) and (node.right is not None):
                if (node.right.data > node.data) and (node.left.data < node.data):
                    self.isBST = True
                    return node.data
                else: 
                    self.isBST = False   
                    print("It is not a BST.")
                    return min,max
            elif node.left is None:
                if node.right.data > node.data:
                    self.isBST = True
                    return node.data
                else: 
                    self.isBST = False   
                    print("It is not a BST.")
                    return min,max
            elif node.right is None:
                if node.left.data < node.data:
                    self.isBST = True
                    return node.data
                else: 
                    self.isBST = False   
                    print("It is not a BST.")
                    return min,max
                
                
    def isBinarySearchTree(self, root, min = -math.inf, max = math.inf ):
        currentNode = root
        if (currentNode is not None) and (self.isBST is True):
            temp = self.checkBinarySubtree(currentNode, min, max)
            if (currentNode.left is not None):
                self.isBinarySearchTree(currentNode.left,min, temp)
            if (currentNode.right is not None):
                self.isBinarySearchTree(currentNode.right, temp, max)
        return self.isBST
        


root = Node(45)
myTree = BinaryTree(root)
myTree.insert(25)
myTree.insert(75)
myTree.insert(15)
myTree.insert(35)

myTree.isBinarySearchTree(root)
