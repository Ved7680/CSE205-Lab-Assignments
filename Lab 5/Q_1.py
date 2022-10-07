'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Bubble sort
'''

def swap(a,b):
    temp = a
    a = b
    b = temp

    return a,b

def Bubble_Sort(arr):
    n = len(arr)

    # To perform operations
    for i in range(n-1):
        # To sort the largest item
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j],arr[j+1])
        
    return arr

myArr = [1,3,5,4,2]
print("Old Array:",myArr)

print("Sorted Array:",Bubble_Sort(myArr))


