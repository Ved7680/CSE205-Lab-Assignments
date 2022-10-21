'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 21-10-22
    Objective: 
    
    Create a 2D array for hashing numbers.
    The hash value decides the row, and the number gets appended to the row
'''      

def Hashing_2D(arr,size):

    hash = [[0]*1 for _ in range(size)]
    # print(hash)

    for i in range(len(arr)):
        m = arr[i]%size
        hash[m].append(arr[i])
    
    return ([k[1:] for k in (hash[0:])])

myarr = [133,174,88,92,221,234]
myhash_2d = Hashing_2D(myarr,12)
print(myhash_2d)