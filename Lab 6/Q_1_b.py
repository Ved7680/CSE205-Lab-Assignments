'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 13-10-22
    Objective: Create a list of numbers (this list should be unique for each student) to demonstrate primary clustering.
'''

def Hash_tables(arr):
    n1 = len(arr)
    hash1 = [-1]*n1

    for i in range(len(arr)):
        pos = arr[i]%n1
        for _ in range(n1):
            if hash1[pos] == -1:
                hash1[pos] = arr[i]
                break
            else:
                pos+=1
    
    return hash1

myarr = [0,2,4,6,8,10]

myhash = Hash_tables(myarr)

print("Primary Clustering:",myhash)

# 0 -> 0
# 2 -> 2
# 4 -> 4
# 6 -> 0 -> 1
# 8 -> 2 -> 3
# 10 -> 4 -> 5