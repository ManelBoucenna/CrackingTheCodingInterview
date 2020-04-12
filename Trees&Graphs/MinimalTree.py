#A minimal binary search tree has same number of kids left and right
# We could start from the middle of every sub-array like in dichotomie
# ex: 1,2,6,|8|,10,15,17 ....Add 8 at root
#     1,|2|,6,|8|,10,15,17   ... Add 2 in left child of root
#     1,|2|,6,|8|,10,|15|,17   ... Add 2 in right child of root  
# etc ...
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self, root=None):
        self.root=root
    def MakeMinimalTree(self, array, root=None):
        middle = int(len(array)/2)
        newNode = Node(array[middle])
        subarrayLeft = array[:middle]
        subarrayRight = array[middle+1:]
        if self.root is None:
                self.root = newNode
        else:
            if (newNode.data<root.data):
                root.left = newNode
            else:
                root.right = newNode
        if subarrayLeft:
            self.MakeMinimalTree(subarrayLeft,newNode)
        if subarrayRight:
            self.MakeMinimalTree(subarrayRight,newNode)

array = [1, 2, 6, 8, 10, 15,17]
BinarySearchTree().MakeMinimalTree(array)
