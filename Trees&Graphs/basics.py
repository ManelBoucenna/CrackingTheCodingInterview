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

    def InOrderSearch(self, root):
        currentNode = root
        if (currentNode is not None):
            self.InOrderSearch(currentNode.left)
            print(currentNode.data, end = ' ')
            self.InOrderSearch(currentNode.right)
    def PreOrderSearch(self,root):
        currentNode = root
        if (currentNode is not None):
            print(currentNode.data, end = ' ')
            self.PreOrderSearch(currentNode.left)
            self.PreOrderSearch(currentNode.right)
    def PostOrderSearch(self,root):
        currentNode = root
        if (currentNode is not None):
            self.PostOrderSearch(currentNode.left)
            self.PostOrderSearch(currentNode.right)
            print(currentNode.data, end = ' ')



root = Node(45)
myTree = BinaryTree(root)
myTree.insert(25)
myTree.insert(75)
myTree.insert(15)
myTree.insert(35)

print("In-order Search")
myTree.InOrderSearch(root)
print("\n Pre-order Search")
myTree.PreOrderSearch(root)
print("\n Post-order Search")
myTree.PostOrderSearch(root)
