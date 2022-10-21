'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 13-10-22
    Objective: Create a list of numbers (this list should be unique for each student) to demonstrate secondary clustering.
'''
def Hash_Tables(arr):
    n = len(arr)
    hash = [-1]*n

    for i in range(len(arr)):
        pos = arr[i]%n
        for j in range(n):
            if hash[pos] == -1:
                hash[pos] = arr[i]
                break
            else:
                pos = (pos + j**2)%n

    return hash

myarr = [0,2,4,6,8,10]

myhash = Hash_Tables(myarr)

print("Secondary Clustering:",myhash)

# 0 -> 0
# 2 -> 2
# 4 -> 4
# 6 -> 0 -> 1
# 8 -> 2 -> 3
# 10 -> 4 -> 5