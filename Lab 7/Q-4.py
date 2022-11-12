'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 12-11-22
    Objective: 
    Implement Binary Search Tree with the following operations:

    Insert
    Remove
    find Minimum ##### You may implement other methods to support the ones mentioned above.
'''

class BinaryTree():
    def __init__(self , Maximum_size):
        self.ele = []
        self.size = 0
        self._len = Maximum_size

    
    def Insert(self, data):

        assert self.size < self._len, " Error! : The Binary Tree is Full :-("

        self.ele.append(data)
        self.size = self.size + 1

        return


    def Remove(self):
        assert self.size>0, " Error! : The Binary Tree is Empty :-("

        root_data = self.ele[0]
        self.size = self.size - 1
        self.ele[0] = self.ele[self.size]

        return root_data

    def Minimum(self):
        fing = Queue()
        fing.Enqueue(0)
        min_e = 0
        while not fing.isEmpty():
            ch = fing.Dequeue()
            if(self.ele[ch]< self.ele[min_e]):
                min_e = ch
            else:
                chleft = (ch*2)+1
                chright = (ch*2)+2
                if chleft < self.size:
                    fing.Enqueue(chleft)
                if chright < self.size:
                    fing.Enqueue(chright)

        return self.ele[min_e]
    
    def disp(self):
        cnt = 0
        j = 1  
        print(" : The Binary Tree : ") 
        for i in range(self.size):  
            print(self.ele[i], end=" ")
            if (i == j-1):
                cnt += 1
                j = j + 2**cnt
                print("")
        print("")



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
    def Enqueue(self, data):
        
        #New QueueNode
        newQueueNode = QueueNode(data)
        
        #Linking New stackNode
        if self.head == None:
            self.head = newQueueNode
            self.tail = newQueueNode
            self.size +=1
        else:
            self.tail.next = newQueueNode
            self.tail = newQueueNode
            self.size +=1
        
    #Dequeue
    def Dequeue(self):
        assert self.tail != None, " Cannot Dequeue from empty Queue :-( "
        data = self.head.data
        self.head = self.head.next
        self.size -=1
        return data


arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
Binary_Tree = BinaryTree(n)
print("\n Inserting the array into the Tree : ", arr,"\n")
for i in range(n):
    Binary_Tree.Insert(arr[i])

Binary_Tree.disp()

print("\n Removing from the tree : ", Binary_Tree.Remove())
print()
print("After removing : The Tree ==> ")
Binary_Tree.disp()

print("\nThe Minimum Element in the Binary Tree : ", Binary_Tree.Minimum(),"\n")