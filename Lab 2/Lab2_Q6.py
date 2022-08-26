'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: a function lsrch(linked_list,element) that searches a linked     list for the element and returns the index (position) in the linked lsit if the element is found, and -1 otherwise.
'''
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def newNode(self,data):
        
        #declaring new node
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

    def lsrch(self,ele):
        curr = self.head
        pos = 1
        while curr != None:
            if curr.data == ele:
                return pos
            curr = curr.next 
            pos+=1

        return -1
    
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
myll.newNode(15)
myll.newNode(2003)

print("The Linked list is given below")
myll.printlist()

print("Position of number '2003' is",myll.lsrch(2003))