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
    def isBalanced(self):
        pass

root = Node(45)
myTree = BinaryTree(root)
myTree.insert(25)
myTree.insert(75)
myTree.insert(15)
myTree.insert(35)

myTree.isBalanced()
