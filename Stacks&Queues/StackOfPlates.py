class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.nextStack = None
    def push(self, data):
        if (self.top==None):
            self.top = Node(data)
        else:
            newNode = Node(data)
            newNode.nextval = self.top
            self.top = newNode
        self.size +=1
            
    def pop(self):
        if self.isEmpty():
            print("The list is empty.")
        else:
           item = self.top.dataval
           self.top =  self.top.nextval
           self.size -=1
           return item
    def isEmpty(self):
        if(self.top == None):
            return True
        else:
            return False
    def isFull(self):
        return (self.size==2)
        
class SetOfStacks:
    def __init__(self):
        self.topStack = None
    def push(self, data):
        if (self.topStack == None):
            newStack = Stack()
            newStack.push(data)
            self.topStack = newStack
        else:
            if (self.topStack.isFull()):
                newStack = Stack()
                newStack.push(data)
                newStack.nextStack = self.topStack
                self.topStack = newStack
            else:
                self.topStack.push(data)
    def pop(self):
        if (self.isEmpty()):
            print('Stack is empty')
        else:
            if (self.topStack.size == 1):
               item = self.topStack.top.dataval
               self.topStack =  self.topStack.nextStack               
            else:
                item = self.topStack.pop()
            return item        
    def peek(self):
        pass
    def isEmpty(self):
        return (self.topStack == None)
    
stacks = SetOfStacks()

stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.pop()
stacks.pop()
