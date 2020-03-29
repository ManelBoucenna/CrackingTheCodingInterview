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
    def Preppend(self, data):
        newNode = Node(data)
        if (self.headval == None):
            self.headval = newNode
            return
        currentNode = self.headval
        while currentNode.nextval is not None:
            currentNode = currentNode.nextval
        currentNode.nextval = newNode
        self.size += 1
       
       
    def isPalindromeWithStack(self):# O(n)
        currentNode = self.headval
        stack = []
        while (currentNode is not None):
            stack.append(currentNode.dataval)
            currentNode = currentNode.nextval
        currentNode = self.headval
        while (currentNode is not None):
            val = stack.pop()
            if (currentNode.dataval != val):
                print("This is not a palindrome")
                return False
            currentNode = currentNode.nextval
        print("This is a palindrome")
        return True

    def isPalindromeWithReversedList(self):# O(n)
        currentNode = self.headval
        ReversedList = SLinkedList()
        while (currentNode is not None):
            ReversedList.Preppend(currentNode.dataval)
            currentNode = currentNode.nextval
        currentNode = self.headval
        while (currentNode is not None):
            val = stack.pop()
            if (currentNode.dataval != val):
                print("This is not a palindrome")
                return False
            currentNode = currentNode.nextval
        print("This is a palindrome")
        return True
    
List = SLinkedList()

List.Append("M")
List.Append("A")
List.Append("Y")
List.Append("A")
List.Append("K")

List.isPalindromeWithStack()
