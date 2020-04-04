class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self, data):
        newNode = Node(data)
        if (self.last != None):
            self.last.nextval = newNode
        self.last = newNode
        if (self.first == None):
            self.first = self.last
            
    def remove(self):
        if (self.isEmpty()):
            print('Queue is empty.')
        else:
            item = self.first.dataval
            self.first = self.first.nextval
            if (self.first == None ):
                self.last = self.first
            return item

    def peek(self):
        if (self.isEmpty()):
            print('Queue is empty.')
        else:
            return self.first.dataval
    def isEmpty(self):
        if (self.first == None):
            return True
        else:
            return False
    
queue = Queue()

queue.add(1)
queue.add(2)
queue.add(3)

queue.remove()
queue.remove()
queue.peek()
