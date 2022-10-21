'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 13-10-22
    Objective: Using Linear Probing, create two hashtables (arrays) of sizes (a) 17 and (b) 37.
    Add the following numbers to both the hashtables (The numbers are written into the array ):

    133, 88, 92, 221, 174

    Now, check if these numbers are in the hashtables or not.

    100,133,174
'''

def Hash_Tables(arr,size):
    hash = [-1]*size

    for i in range(len(arr)):
        pos = arr[i]%size
        for j in range(size):
            if hash[pos] == -1:
                hash[pos] = arr[i]
                break
            else:
                pos = (pos + j**2)%size

    return hash

def Searching(hash,ele):
    n = len(hash)
    pos = ele%n

    i=0
    while pos != None:
        if pos == n:
            pos = 0
        if hash[pos] == ele:
            return True
        if pos == ele%n:
            break
        i+=1
        pos = (pos + (i)**2)%n
    
    return False

myarr = [133,88,92,221,174]

myhash1 = Hash_Tables(myarr,17)
myhash2 = Hash_Tables(myarr,37)

print(myhash1)
print()
print(myhash2)
print(Searching(myhash1,92))