class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
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
        
class MyQueue:#Lazy approach
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
    def add(self, data):
            self.stack_one.push(data)
    def remove(self):
        while (self.stack_one.top):
            item = self.stack_one.pop()
            self.stack_two.push(item)
        self.stack_two.pop()
        while (self.stack_two.top):
            item = self.stack_two.pop()
            self.stack_one.push(item)
        
    
myQueue = MyQueue()

myQueue.add(1)
myQueue.add(2)
myQueue.add(3)
myQueue.remove()
myQueue.remove()
