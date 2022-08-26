'''
    AUTHOR: Ved J Nayi
    DOC: 18-08-22
    Objective: Write a function insatend(array,element) that inserts an element at the end of an
               array.
'''

def insatend(arr,ele):
    length = len(arr)+1
    mylist = [0]*length
    for i in range(len(arr)):
        mylist[i] = arr[i]

    mylist[len(arr)] = ele
    return mylist

print(insatend([1,3,5],6))