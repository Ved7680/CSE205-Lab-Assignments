'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Insertion sort using Binary Search. Also, comparing Insertion Sort Timings for linear serach and binary search
'''

import time

# Using Binary Search

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


def Bin_Insertion_Sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        pos = Binary_Search(arr,temp,0,i)+1 

        for j in range(i,pos,-1):
            arr[j] = arr[j-1]
        arr[pos] = temp

    return arr

myArr = [45,32,3,4,98,78,64,34,1]
print("Old Array:",myArr)

print("Sorted Array:",Bin_Insertion_Sort(myArr))

# Using Linear Search

def Lin_Insertion_Sort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        k = i
        while temp <= arr[k-1] and k > 0 :
            arr[k] = arr[k-1]
            k -=1
        arr[k] = temp
    return arr

# myArr2 = [45,32,3,4,98,78,64,34,1]
# print("Old Array:",myArr)
# print("Sorted Array:",Lin_Insertion_Sort(myArr))

# Comparing time between both of them
Bin_Insertion_Sort(myArr)
t1 = time.perf_counter()
Lin_Insertion_Sort(myArr)
t2 = time.perf_counter()

t_diff = t1 - t2

print()
print("Difference between running time of Binary Insertion Sort and Linear Insertion Sort is",t_diff)
print()

# Output is negative because t2 > t1



