'''
    AUTHOR: Ved J Nayi
    DOC: 6-10-22
    Objective: Implementing Radix sort
'''

class QNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head is None
    
    def len(self):
        return self.count

    def enQueue(self,data):
        newNode = QNode(data)

        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode  # type: ignore
        
        self.tail = newNode
        self.count+=1
    
    def deQueue(self):
        if not self.isEmpty():
            newNode = self.head

            if self.head is self.tail:
                self.tail = None
            
            self.head = self.head.next  # type: ignore
            self.count-=1

            return newNode.data     # type: ignore


def Radix_Sort(arr,num_digits):
    bin_arr = [0]*10
    for i in range(10):
        bin_arr[i] = Queue()    # type: ignore
    
    col = 1

    for j in range(num_digits):
        for ele in arr:
            digit = (ele//col)%10
            bin_arr[digit].enQueue(ele) # type: ignore
        
        k=0
        for bin in bin_arr :
            while not bin.isEmpty() :   # type: ignore
                arr[k] = bin.deQueue()  # type: ignore
                k += 1
        col *= 10
    
    return arr

myarr = [10, 7, 8, 9, 1, 5]
print("Old Array:",myarr)
Radix_Sort(myarr, 2)
print("Sorted Array:",myarr)

# Here, #type: ignore is used to remove warnings
