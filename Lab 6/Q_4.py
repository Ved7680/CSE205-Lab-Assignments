'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 20-10-22
    Objective: 
    Create two hashtables (arrays) of size 17 and 37.

    This time, each hashtable is an array of bits.

    There are two arrays of 17 bits and 37 bits, all initialised to 0 (zero).

    Consider the following number: 142.
        142%17 = 6
        142%37 = 31
        142 is "added" to the hashtable by setting to 1 the 6th and the 31st bit of the two hashtables respectively.
        To check if 142 is in the list, just check if 6th (in the first) and 31st (in the second) are set to 1.

    Add the following numbers:
        133, 88, 92, 221, 174

    Check if these numbers are in the hashtable or not:
        100, 133, 174

'''

def Hash_Tables(arr,size):
    hash = [0]*size

    for i in range(len(arr)):
        pos = arr[i]%size
        for _ in range(size):
            if hash[pos] == 0:
                hash[pos] += 1
                break
            else:
                pos+=1

    return hash

def Searching(hash,ele):
    n = len(hash)
    pos = ele%n

    i=0
    while pos != None:
        if pos == n:
            pos = 0
        if hash[pos] == 1:
            return True
        if pos == ele%n:
            break
        i+=1
        pos +=1
    
    return False

myarr = [133,88,92,221,174]

myhash1 = Hash_Tables(myarr,17)
myhash2 = Hash_Tables(myarr,37)

print(myhash1)
print()
print(myhash2)
print(Searching(myhash1,92))
print(Searching(myhash2,26))

# Here 26 in not in myhash2 but 26%37 = 174%37. SO, it considers that 26 is in the hash table.