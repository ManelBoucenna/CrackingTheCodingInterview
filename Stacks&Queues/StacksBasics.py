class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 1
    def push(self, data):
        if (self.top==None):
            self.top = Node(data)
        else:
            newNode = Node(data)
            newNode.nextval = self.top
            self.top = newNode
            
    def pop(self):
        if self.isEmpty():
            print("The list is empty.")
        else:
           item = self.top.dataval
           self.top =  self.top.nextval
           return item

    def peek(self):
        if self.isEmpty():
            print("The list is empty.")
        else:
           return self.top.dataval
    
    def isEmpty(self):
        if(self.top == None):
            return True
        else:
            return False
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.pop()

stack.peek()
