'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 04-09-22
    Objective: Implementing stacks using linked list
'''
# Defining a stack node for linked list
class StackNode():
    def __init__(self,item):
        self.item = item
        self.next = None

class Stacks():
    # Initialization of stack
    def __init__(self):
        self.top = None
    
    # Checking whether the stack is empty or not
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    # Getting the number of items in stack
    def len(self):
        return self.size

    # Only seeing the top element of stack
    def peek(self):
        if self.isEmpty():
            print("!!Stack is Empty!!")
        else:
            return self.top.item

    # returns The uppermost (or top) element of stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            pop_node = self.top
            self.top = self.top.next
            pop_node.next = None
            return pop_node.item

    # Adds an element at the top of stack
    def push(self,item):
        if self.top == None:
            self.top = StackNode(item)
        else:
            newNode = StackNode(item)
            newNode.next = self.top
            self.top = newNode
    
    # To display the whole stack
    def Disp(self):
        node = self.top
        if self.isEmpty():
            print("!!Stack Underflow!!")
        else:
            while(node!=None):
                print(node.item,"--->",end = ' ')
                node = node.next
                
myS = Stacks()

myS.push(97)
myS.push(24)
myS.push(13)
myS.Disp()
print()
print(myS.pop())
print(myS.peek())