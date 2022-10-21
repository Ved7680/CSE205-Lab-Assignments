'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 13-10-22
    Objective: Using Linear Probing, create two hashtables (arrays) of sizes (a) 17 and (b) 37.
    Add the following numbers to both the hashtables (The numbers are written into the array ):

    133, 88, 92, 221, 174

    Now, check if these numbers are in the hashtables or not.

    100,133,174
'''
def Hash_tables(arr):
    hash1 = [-1]*17
    hash2 = [-1]*37

    n1 = len(hash1)
    n2 = len(hash2)

    for i in range(len(arr)):
        pos1 = arr[i]%n1
        for _ in range(n1):
            if hash1[pos1] == -1:
                hash1[pos1] = arr[i]
                break
            else:
                pos1+=1

    # flag = 0
    # for j in range(len(arr)):
    #     dup1 = arr[j]%n1
    #     for k in range(len(arr)):
    #         if hash1[k] == ele:
    #             flag = 1
    #             break
    #         # else:
    #         #     dup1 +=1

    # if flag == 1:
    #     print("Element Exists")
    # else:
    #     print("Element Does Not Exists")

    for i in range(len(arr)):
        pos2 = arr[i]%n2
        for _ in range(n2):
            if hash2[pos2] == -1:
                hash2[pos2] = arr[i]
                break
            else:
                pos2+=1

    # flag = 0
    # for j in range(len(arr)):
    #     dup1 = arr[j]%n1
    #     for k in range(len(arr)):
    #         if hash1[k] == ele:
    #             flag = 1
    #             break
    #         # else:
    #         #     dup1 +=1

    # if flag == 1:
    #     print("Element Exists")
    # else:
    #     print("Element Does Not Exists")

    return hash1,hash2

def Searching(hash,ele):
    n = len(hash)
    pos = ele%n

    while pos != None:
        if pos == n:
            pos = 0
        if hash[pos] == ele:
            return True
        if pos+1 == ele%n:
            break
        pos += 1
    
    return False
    
myarr = [133,88,92,221,174]

myhash1, myhash2 = Hash_tables(myarr)

print("First Hash Table:",myhash1)
print()
print("Second Hash Table:",myhash2)

x = Searching(myhash1,100)
y = Searching(myhash2,133)

print(x)
print(y)
# 133 -> 14
# 88 -> 3
# 92 -> 7
# 221 -> 0
# 174 -> 4