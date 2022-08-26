'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-08-22
    Objective: a function replatind(array,position,element) to replace an element into an
               array at the specified index (position).
'''

def replatind(arr,pos,ele):
    mylist = [0]*len(arr)

    for i in range(len(arr)):
        if i == pos - 1:
            mylist[i] = ele
        else:
            mylist[i] = arr[i]
    
    if pos > len(arr):
        return -1
    else:
        return mylist

print(replatind([1,2,3,4,5],3,15))