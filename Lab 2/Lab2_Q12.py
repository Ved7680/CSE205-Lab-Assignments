'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: a function dubbly_remove(dlinked_list,element) to remove an element from
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

    def newNode(self,data):
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
        while curr != None:
            if curr.next is None:
                print(curr.data)
            else:
                print(curr.data,end=' <===> ')
            curr = curr.next

    def dubbly_remove(self,ele):
        cur = self.head
        curp = None
        if cur.data == ele:
            self.head = cur.next
            print("\nThe New Linked List : ")
            return DoubleLinkedList.printlist(self)
        else:
            curp = cur
            cur = cur.next
            c = -1
            while cur != None:
                # Checking for last Node 
                if cur.data == ele:
                    curp.next = cur.next
                    cur.prev = curp
                    c = 1
                    print("\nThe New Linked List : ")
                    return DoubleLinkedList.printlist(self)
                curp = cur
                cur = cur.next
            if c == -1:
                return(print("-1"))


dl = DoubleLinkedList()
dl.newNode(10)
dl.newNode(11)
dl.newNode(12)
dl.newNode(13)
dl.newNode(14)

# Printing the linked list
print("The Linked List : ")
dl.printlist()

# Adding element at the end and printing the linked list
dl.dubbly_remove(10)