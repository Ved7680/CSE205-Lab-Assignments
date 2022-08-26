'''
    AUTHOR: Ved J Nayi
    DOC: 18-08-22
    Objective: a function delatind(array,position) to delete the element at the specified
               index (position) in the array.
'''

def delatind(arr,pos):
    length = len(arr)-1
    mylist = [0]*length
    j=0
    for i in range(len(arr)):
        if i == pos-1:
            pass
        else:
            mylist[j] = arr[i]
            j+=1
    
    return mylist

print(delatind([1,2,3,4,5],3))