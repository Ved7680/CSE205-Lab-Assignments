'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 16-09-22
    Objective: Checking for balanced Parenthesis using Stacks
'''

class StackNode :
    def __init__(self, data) :
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.head = None
        self.size = 0

    # Returns boolean expression
    def isEmpty(self):
        return (self.head == None)

    #returns the size of the stack
    def len_(self):
        return self.size 
    
    def validation(self):
        mystr = input("Enter : ")
        oc = ["(","[","{"]
        mystr = mystr.replace(" ","")
        for i in range(len(mystr)):
            if(mystr[i] == "/" and mystr[i+1] == "/"):
                break 
            if(mystr[i] in oc):
                Stack.push(self, mystr[i])
            else:
                if(mystr[i] == ")"):
                    if (Stack.peek(self) != "(" or Stack.isEmpty == True):
                        Stack.push(self,1)
                        Stack.disp(self)
                        break
                    a = Stack.pop(self)
                if(mystr[i] == "]"):
                    if (Stack.peek(self) != "[" or Stack.isEmpty == True):
                        Stack.push(self,1)
                        Stack.disp(self)
                        break
                    a = Stack.pop(self)
                if(mystr[i] == "}"):
                    if (Stack.peek(self) != "{" or Stack.isEmpty == True):
                        Stack.push(self,1)
                        Stack.disp(self)
                        break
                    a = Stack.pop(self)                    
        if(Stack.isEmpty(self) == True):
            print("String is Balanced")
            return " "
        else:
            return "String is Unbalanced"

    #Push Stack
    def push(self, data):
        
        #New StackNode
        newStackNode = StackNode(data)
        
        #Linking New stackNode
        if self.head == None:
            self.head = newStackNode
            self.size +=1
        else:
            newStackNode.next = self.head
            self.head = newStackNode
            self.size +=1
        
    #Pop Stack
    def pop(self):
        # assert self.head != None, " Cannot pop from empty stack :-( "
        data = self.head.data
        self.head = self.head.next
        self.size -=1
        return data
    
    # the peek of the Stack
    def peek(self):
        # assert self.head != None, "Empty stack does not hav peek :-( "
        return self.head.data

    
    # Printing the Sack
    def disp(self):
        cur = self.head
        print("\n The Stack : ")
        for i in range(Stack.len_(self)):
            print(cur.data)
            cur = cur.next

sp = Stack()
print(sp.validation())
