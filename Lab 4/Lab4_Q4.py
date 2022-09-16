'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 04-09-22
    Objective: Implementing queues using linked list
'''

class QNode:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def isempty(self):
        return self.front == None
    
    def enQueue(self,data):
        temp = QNode(data)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        if self.isempty():
            return
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

myQ = Queue()
myQ.enQueue(15)
myQ.enQueue(10)
myQ.enQueue(2003)
myQ.deQueue()

print("Queue Front:",myQ.front.data)
print("Queue Rear:",myQ.rear.data)