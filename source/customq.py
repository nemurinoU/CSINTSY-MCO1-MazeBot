"""
customq.py

Really, it's just a self implementation of a Queue.

Author(s):  Martinez, Francis Benedict V.
            
Version:    0.0.1
Date:       2023-02-22
"""
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def enqueue (self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def pop (self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            pass
    
    def show (self):
        print (self.queue)