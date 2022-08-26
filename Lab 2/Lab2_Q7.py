'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: function linsatend(linked_list,element) that inserts an element at the end
               of a linked list.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def newNode(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode 
    
    def linsatend(self,ele):
        newNode = Node(ele)

        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printlist(self):
        curr = self.head
        while curr != None:
            if curr.next is None:
                print(curr.data)
            else:
                print(curr.data , end=' ---> ')
            curr = curr.next

myll = LinkedList()
myll.newNode(10)
myll.newNode(3)
myll.newNode(1980)

print("The Linked list is given below")
myll.printlist()

print("The Linked List after inserting an element at end")
myll.linsatend(1976)
myll.printlist()
    