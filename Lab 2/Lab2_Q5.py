'''
    AUTHOR: Ved J Nayi
    DOC: 18-08-22
    Objective: a function insatbeg(array,element) that inserts an element at the beginning
               of the array.
'''

def insatbeg(arr,ele):
    length = len(arr)+1
    mylist = [0]*length
    
    mylist[0] = ele

    for i in range(1,len(arr)+1):
        mylist[i] = arr[i-1]

    return mylist

print(insatbeg([1,2,3,4,5,89],10))