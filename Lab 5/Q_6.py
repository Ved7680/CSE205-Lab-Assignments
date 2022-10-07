'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Quick sort where pivot is always the middle element
'''

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

def Parttiton_Middle(arr,start,end):
    mid_pivot = (start+end)//2

    arr[start], arr[mid_pivot] = arr[mid_pivot], arr[start]

    return Partition(arr,start,end)

def Quick_Sort(arr,start,end):
    if start < end:
        pivot = Parttiton_Middle(arr,start,end)
        Quick_Sort(arr,start,pivot)
        Quick_Sort(arr,pivot+1,end)
    
myArr = [45,32,3,4,98,78,64,34,1]
print("Old Array:",myArr)
Quick_Sort(myArr,0,len(myArr)-1)
print("Sorted Array:",myArr)
        