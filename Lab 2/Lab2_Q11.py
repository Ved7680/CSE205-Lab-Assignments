'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: a function dubbly_append(dlinked_list,element) to append an element into
               the doubly linked list.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def dubbly_append(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail.next.prev = self.tail
            self.tail = newNode

    def printlist(self):
        curr = self.head
        while curr!=None:
            if curr.next is None:
                print(curr.data)
            else:
                print(curr.data,end=' <===> ')
            curr = curr.next
    
mydl = DoubleLinkedList()
mydl.dubbly_append(10)
mydl.dubbly_append(3)
mydl.dubbly_append(1980)
mydl.dubbly_append(1976)
mydl.dubbly_append(2003)

print("The Doubly Linked list is given below")
mydl.printlist()
