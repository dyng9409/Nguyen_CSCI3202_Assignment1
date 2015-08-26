#implementation of queue
import Queue

class queue(object):
    #basically a wrapper class for the python Queue module

    def __init__(self):
        self.q = Queue.Queue()

    def check_int(self, val):
        #check to make sure queue is only Integers
        if(type(val) is int):
            return True;
        else:
            return False;

    def push(self, val):
        #adding a value to the queue
        #no return value
        if self.check_int(val):
            self.q.put(val)
        else:
            print('Only integers are accepted')

    def pop(self):
        #returns the first item in the queue
        return self.q.get()

    def checkSize(self):
        #returns the current size of the queue
        return self.q.qsize()

    def isEmpty(self):
        #checks if queue is empty
        return self.q.empty()

