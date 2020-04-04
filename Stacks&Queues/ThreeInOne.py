# Not available in python because we don't have to predefine size
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class ArrayStack:
    def __init__(self):
        self.size = 0
        self.stack = []
        self.index = {
            1: None,
            2: None,
            3: None
            }
    def push(self, List, data):
        if (List == 1):
            if (self.index[List] == None):
                self.index[List] = 0
                self.stack.append(data)
            else:
                temp1 = self.stack[:self.index[List]-1]
                temp2 = self.stack[self.index[List]:]
                temp2.append(data)
                self.stack = temp1 + temp2
                self.index[List] += 1
                if (self.index[List+1]): 
                    self.index[List+1] += 1
                if (self.index[List+2]): 
                    self.index[List+2] += 1
        elif (List == 2):
            if (self.index[List] == None):
                self.index[List] = self.index[List-1]+1
                self.stack.append(data)
            else:
                temp1 = self.stack[:self.index[List]+1]
                temp2 = self.stack[self.index[List]+2:]
                temp1.append(data)
                self.stack = temp1 + temp2
                self.index[List] += 1
                if (self.index[List+1]): 
                    self.index[List +1] += 1
        else:
            if (self.index[List] == None):
                self.index[List] = self.index[List-1]+1
                self.stack.append(data)
            else:
                self.stack.append(data)
                self.index[List] += 1
            
    def pop(self,List):
        pass
    def peek(self):
        pass
    def isEmpty(self):
        pass
    
arrayStack = ArrayStack()

arrayStack.push(1,1)
arrayStack.push(1,2)
arrayStack.push(2,'A')
arrayStack.push(2,'B')
arrayStack.push(3,'+')
arrayStack.push(3,'-')
