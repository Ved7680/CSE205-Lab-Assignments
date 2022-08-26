'''
    AUTHOR: Ved J Nayi
    DOC: 18-08-22
    Objective: a function srch(array,element) that searches the array for the element and
               returns the index (position) in the array if the element is found, and -1 otherwise
'''

def srch(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i+1
        
    return -1

print("Position:",srch([1,2,3,4,5],3)) # Ans = Position: 3
print("Position:",srch([1,2,3,4,5],7)) # Ans = Position: -1


        

