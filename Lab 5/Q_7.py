'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Quick sort where pivot is chosen Randomly
'''

import random   

def Partition(arr,start,end):
    pivot = start
    i = start - 1
    j = end + 1

    while True:
        while True:
            i+=1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j-=1
            if arr[j] <= arr[pivot]:
                break
        if i>=j:
            return j 
        arr[i], arr[j] = arr[j] ,arr[i]

def Parttiton_Rand(arr,start,end):
    rand_pivot = random.randrange(start,end)

    arr[start], arr[rand_pivot] = arr[rand_pivot], arr[start]

    return Partition(arr,start,end)

def Quick_Sort(arr,start,end):
    if start < end:
        pivot = Parttiton_Rand(arr,start,end)
        Quick_Sort(arr,start,pivot)
        Quick_Sort(arr,pivot+1,end)

myarr = [10, 7, 8, 9, 1, 5]
print("Old Array:",myarr)
Quick_Sort(myarr, 0, len(myarr) - 1)
print("Sorted Array:",myarr)