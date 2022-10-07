'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Comparing the Time for Worst and Best Cases of Selection and Insertion Sort
'''

# import timeit
import time

# ------------------------ For Selection Sort------------------------------------- 
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


def Selec_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        # Assuming the smallest element has i index
        min_ind = i

        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind = j

        if min_ind != i:
            arr[i],arr[min_ind] = swap(arr[i],arr[min_ind])
        
    return arr

# ------------------------ For Insertion Sort------------------------------------- 

def Binary_Search(arr,ele,start,end):

    if end - start <= 1:
        if ele < arr[start]:
            return start - 1
        else:
            return start
    mid = (start+end) // 2

    if arr[mid] < ele:
        return Binary_Search(arr, ele, mid, end)
    elif arr[mid] > ele:
        return Binary_Search(arr, ele, start, mid)
    else:
        return mid


def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        pos = Binary_Search(arr,temp,0,i)+1 

        for j in range(i,pos,-1):
            arr[j] = arr[j-1]
        arr[pos] = temp

    return arr

myArr1 = [1,2,3,4,5]
myArr2 = [5,4,3,2,1]

# print("Time for Best Cases:")
# print("For Selection Sort:",end=' ')
Selec_Sort(myArr1)
tic1 = time.perf_counter()
Insertion_Sort(myArr1)
toc1 = time.perf_counter()
# print("",toc-tic)

Selec_Sort(myArr2)
tic2 = time.perf_counter()
Insertion_Sort(myArr2)
toc2 = time.perf_counter()


print("Best Case for Selection Sort:",tic1)
print("Best Case for Insertion Sort:",toc1)
print()
print("Worst Case for Selection Sort:",tic2)
print("Worst Case for Insertion Sort:",toc2)
