'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 21-10-22
    Objective: 
    
    Using Double Hashing, create one hashtable (array) with M = 17, P = 11.

    Add the following numbers to the hashtables (The numbers are written into the array ):
        133, 88, 92, 221, 174

    Now, check if these numbers are in the hashtables or not.
        100, 133, 174

'''

def Hash_Tables(arr,size):
    m=17
    p=11

    hash = [-1]*size

    for i in range(len(arr)):
        pos = arr[i]%size
        for j in range(size):
            if hash[pos] == -1:
                hash[pos] = arr[i]
                break
            else:
                pos = (pos + j * ( 1 + ( arr[i] % p ) ) ) % m

    return hash

def Searching(hash,ele):
    m = 17
    p = 11
    check = ele%m
    j = 1

    while check != None and j<len(hash):
        if(hash[check]==ele):
            return True
        check = (ele%m + (j + ele%p))%m
        j += 1

    return False

myarr = [133,88,92,221,174]

myhash = Hash_Tables(myarr,17)

print(myhash)
print(Searching(myhash,100))
print(Searching(myhash,133))
print(Searching(myhash,174))