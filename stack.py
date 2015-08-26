#implementation of a stack data structure using 
#python lists

class stack(object):

    def __init__(self):
        self.stk = []
        self.size = 0
    
    def checkInt(self, val):
        #checks argument for int type
        if (type(val) is int):
            return True
        else: 
            return False 
        
    def checkSize(self): 
        #gets size of the stack
        return self.size 

    def checkEmpty(self):
        #checks if the stack is empty
        return (self.checkSize() == 0)

    def push(self, val): 
        #pushes a value val onto the stack and increments the size
        if self.checkInt(val): 
            self.stk.append(val)
            self.size += 1
        else:
            print('Stack only accepts integer values')
        return

    def pop(self):
        #removes and returns the last value added to the stack
        if self.checkEmpty():
            print('Stack is empty')
            return 0;
        else:
            self.size -= 1
            return self.stk.pop()
