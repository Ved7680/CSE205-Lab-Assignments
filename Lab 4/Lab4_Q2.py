'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 16-09-22
    Objective: Taking a postfix expression from user and evaluating it
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

def Postfix_Evaluate(s):
    s = s.split()
    n = len(s)
    myStack = Stacks()

    for i in range(n):
        if s[i].isdigit():
            myStack.push(int(s[i]))
        elif s[i] == '+':
            num1 = myStack.pop()
            num2 = myStack.pop()
            ans = int(num1) + int(num2)
            myStack.push(ans)
        elif s[i] == '-':
            num1 = myStack.pop()
            num2 = myStack.pop()
            ans = int(num1) - int(num2)
            myStack.push(ans)
        elif s[i] == '*':
            num1 = myStack.pop()
            num2 = myStack.pop()
            ans = int(num1) * int(num2)
            myStack.push(ans)
        elif s[i] == '/':
            num1 = myStack.pop()
            num2 = myStack.pop()
            ans = int(num1) / int(num2)
            myStack.push(ans)
    
    return myStack.pop()

# Space is required to solve two or more digits

mystr = "10 2 8 * + 3 -"
res = Postfix_Evaluate(mystr)
print(res)  # res = 3 - ((2*8) + 10) = -23