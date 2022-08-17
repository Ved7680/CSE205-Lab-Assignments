"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: getting product of elements of array using a fuction prodArray()
"""

def prodArray(myList):
    l = []
    if len(myList)==0:
        return 1
    else:
        num = myList.pop(len(myList)-1)
        l.append(num)
        x = l[0]*prodArray(myList)
        return x

ans = prodArray([2,3,5])
print("Product of Array:",ans)
        


