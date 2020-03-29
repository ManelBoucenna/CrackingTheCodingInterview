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
        newNode.nextval = self.headval
        self.headval = newNode
       
       
    def isPalindromeWithString(self):# O(n)
        currentNode = self.headval
        s = ""
        while (currentNode is not None):
            s+=currentNode.dataval
            currentNode = currentNode.nextval
        if (s!=s[::-1]):
            print("This is not a palindrome")
            return False
        else:
            print("This is a palindrome")
            return True
            
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
        ReversedNode = ReversedList.headval
        while (currentNode is not None):
            if (currentNode.dataval != ReversedNode.dataval):
                print("This is not a palindrome")
                return False
            currentNode = currentNode.nextval
            ReversedNode = ReversedNode.nextval
        print("This is a palindrome")
        return True
        
    def isPalindromeWithDoublePointers(self):# O(n)
        p = self.headval
        q = self.headval
        prevs = []
        i=0
        while(q):
            prevs.append(q)
            q=q.nextval
            i+=1   
        count = 1
        while (count<=i//2+1):
            if (p.dataval != prevs[-count].dataval):
                print("This is not a palindrome")
                return False
            p = p.nextval
            count+=1
        print("This is a palindrome")
        return True
    
List = SLinkedList()

List.Append("K")
List.Append("A")
List.Append("Y")
List.Append("A")
List.Append("K")

List.isPalindromeWithDoublePointers()
