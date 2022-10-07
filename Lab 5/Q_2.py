'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Selection sort
'''
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

myArr = [1,3,5,4,2]
print("Old Array:",myArr)

print("Sorted Array:",Selec_Sort(myArr))