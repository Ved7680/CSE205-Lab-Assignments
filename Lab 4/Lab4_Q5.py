'''
    AUTHOR: Ved J Nayi
    DOC: 11-09-22
    Objective: Implementing the Priority Queue ADT using unsorted linked list.
'''

class PQNode:
    def __init__(self,data,prior):
        self.data = data
        self.prior = prior
        self.next = None

class PQueue:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def enQueue(self,value,pr):
        newNode = PQNode(value,pr)  # Creating a new Node

        if self.isEmpty() == True:  # Cheking whether the PQueue is Empty or not
            self.head = newNode     # Storing the value in PQueue
        else:
            if self.head.prior > pr:    # Checking whether the first Node priority is greater than newNode priority or not
                newNode.next = self.head    # making the newNode as 1st Node

                self.head = newNode     # Assigning the newNode as head

                return 1
            else:
                currNode = self.head    # Checking the whole list for other lower priority number

                while currNode.next:

                    if pr <= currNode.next.prior:   #If found then current node will come after previous node
                        break
                    currNode = currNode.next

                newNode.next = currNode.next
                currNode.next = newNode

                return 1
        
    def deQueue(self):
        
        if self.isEmpty() == True:
            return 
        else:
            self.head = self.head.next  # Removing the 1st element of PQueue
            return 1

    def peek(self):

        if self.isEmpty() == True:  # Checking whether the Priority Queue is Empty or Not
            return
        else:
            return self.head.data   # Returns the 1st element of List
    
    def Traverse(self):     # Will print every value of Priority Queue
        if self.isEmpty() == True:              
            return "Priority Queue is Empty"
        else:
            currNode = self.head
            while currNode:
                print(currNode.data,end=' ')
                currNode = currNode.next


pq = PQueue()
pq.enQueue(4, 1)
pq.enQueue(5, 2)
pq.enQueue(6, 3)
pq.enQueue(7, 0)

pq.Traverse()
pq.deQueue()
print()
print(pq.peek())
pq.Traverse()


                    
