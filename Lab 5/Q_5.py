'''
    AUTHOR: Ved J Nayi
    DOC: 29-09-22
    Objective: Implementing Merge sort
'''
def Merge_Sorted_Seq(arr,left,right,end,tempArr):
    num1 = left
    num2 = right
    
    j=0
    while num1 < right and num2 < end:
        if arr[num1] < arr[num2]:
            tempArr[j] = arr[num1]
            num1+=1
        else:
            tempArr[j] = arr[num2]
            num2+=1
        j+=1
    
    while num1 < right:
        tempArr[j] = arr[num1]
        num1+=1
        j+=1

    while num2 < end:
        tempArr[j] = arr[num2]
        num2+=1
        j+=1
    
    for i in range(end - left):
        arr[i+left]  = tempArr[i]


def Rec_Merge_Sort(arr,start,end,tempArr):
    if start == end:
        return
    else:
        mid = (start+end)//2

    Rec_Merge_Sort(arr,start,mid,tempArr)
    Rec_Merge_Sort(arr,mid+1,end,tempArr)

    Merge_Sorted_Seq(arr,start,mid+1,end+1,tempArr)

def Merge_Sort(arr):
    n = len(arr)
    tempArr = [0]*n

    Rec_Merge_Sort(arr,0,n-1,tempArr)
    return tempArr

myArr = [1,3,5,4,2,7,6,10,9,8]
print("Old Array:",myArr)

print("Sorted Array:",Merge_Sort(myArr))
