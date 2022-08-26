'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: a function replatind(linked_list,position,element) to replace an element into an
               linked_list at the specified index (position).
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
    
    def printlist(self):
        curr = self.head
        while curr!=None:
            if curr.next is None:
                print(curr.data)
            else:
                print(curr.data,end=' ---> ')
            curr = curr.next
    
    def replatind(self,pos,ele):
        curr = self.head
        dup = self.head
        ind = 0
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        
        if pos <= count:
            while dup != None:
                if pos <= count:
                    if ind == pos-1:
                        dup.data = ele
                        return 1
                    ind+=1
                    dup = dup.next
        else:
            return -1

myll = LinkedList()
myll.newNode(10)
myll.newNode(3)
myll.newNode(1980)
myll.newNode(1976)
myll.newNode(2003)

print("The Linked list is given below")
myll.printlist()

num = int(input("Enter the new number: "))
pos = int(input("Enter the position at which the number is to replaced: "))

x = myll.replatind(num,pos)
print("The Linked list after replacing the specific element is given below")
if x == 1:
    myll.replatind(num,pos)
    myll.printlist()
else:
    print(-1)
                

