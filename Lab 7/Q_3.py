'''
    AUTHOR: Ved J Nayi
    DOC: 12-11-22
    Objective: Implement Heapsort algorithm using Minheap.
'''

class MinHeap():
    def __init__(self , Maximum_size):
        self.ele = []
        self.size = 0
        self._len = Maximum_size

    
    def len(self):
        return self.size

    
    def Add_Node(self, data):

        assert self.size < self._len, " Error! : The Heap is Full :-("

        self.ele.append(data)
        self.size = self.size + 1
        self.move_up(self.size-1)

        return


    def move_up(self,_index):
        if _index == 0:
            return
        if _index > 0 :
            p = (_index - 1) // 2 
               
        if (self.ele[_index] < self.ele[p]): 
            self.ele[_index], self.ele[p] = self.ele[p], self.ele[_index]
            self.move_up(p)
        
        return


    def Delete_Node(self):
        assert self.size>0, " Error! : The Heap is Empty :-("

        root_data = self.ele[0]
        self.size = self.size - 1
        self.ele[0] = self.ele[self.size]
        self.move_down(0)

        return root_data
    
    def move_down(self, _index):

        left_child = (2*_index) + 1
        right_child = (2*_index) + 2

        if(left_child < self.size and self.ele[_index] >= self.ele[left_child]):

            tmp = self.ele[left_child]
            self.ele[left_child] = self.ele[_index]
            self.ele[_index] = tmp
            self.move_down(left_child)
        
        if(right_child < self.size and self.ele[_index] >= self.ele[right_child]):

            tmp = self.ele[right_child]
            self.ele[right_child] = self.ele[_index]
            self.ele[_index] = tmp
            self.move_down(right_child)
        
        return

arr = [10,9,8,7,6,5,4,3,2,1]
n = len(arr)
print("\nUnsorted Array : ",arr)

sort_heap = MinHeap(n)
for i in range(n):
    sort_heap.Add_Node(arr[i])

for j in range(n):
    arr[j] = sort_heap.Delete_Node()

print("Sorted Array : ",arr)
