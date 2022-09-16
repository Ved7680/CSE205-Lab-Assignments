'''
    AUTHOR: Ved J Nayi
    DOC: 11-09-22
    Objective: A deque (pronounced “deck”) is similar to a queue, except that elements can be enqueued at either end and dequeued from either end. Define a Deque ADT and then provide an implementation for your definition.
'''

class QueueNode :
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Returns boolean expression
    def isEmpty(self):
        return (self.head == None)

    #returns the size of the Queue
    def length_(self):
        return self.size 

    #Enqueue
    def enqueue(self,data):
        
        #New QueueNode
        newQueueNode = QueueNode(data)
        
        #Linking New stackNode
        if self.tail == None:
            self.head = newQueueNode
            self.tail = newQueueNode
            self.size +=1
        else:
            self.tail.next = newQueueNode
            self.tail = newQueueNode
            self.size +=1
    
    def frontenqueue(self,data):
         #New QueueNode
        newQueueNode = QueueNode(data)

       #Linking New stackNode 
        if self.head == None:
            self.tail  = newQueueNode
            self.head = newQueueNode
        else:
            newQueueNode.next = self.head
            self.head = newQueueNode
        self.size +=1
        
    #dequeue
    def dequeue(self):
        assert self.tail != None, " Cannot dequeue from empty Queue :-( "
        data = self.head.data
        self.head = self.head.next
        self.size -=1
        return data

    def reardequeue(self):
        assert self.tail != None, " Cannot dequeue from empty Queue :-( "
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
        print("Rear dequeued data : ",cur.data)
        cur.next = None
        self.tail = cur
        self.size -=1
        return " "
  
    # Printing the Queue
    def disp(self):
        cur = self.head
        print("\n The Queue : ")
        for i in range(Queue.length_(self)):
            print(cur.data,end=" ")
            cur = cur.next
            

qu = Queue()
qu.length_()
qu.enqueue(12)
qu.enqueue(13)
qu.enqueue(14)
qu.enqueue(15)
qu.disp()
print("\nIs the Queue empty? : ",qu.isEmpty())
print("\nThe length of the Queue : ",qu.length_())
print("\nThe dequeued item :\n ",qu.dequeue())
print("\nThe dequeued item :\n ",qu.dequeue())
qu.disp()
qu.frontenqueue(10)
qu.disp()
qu.reardequeue()
qu.disp()