'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-10-22
    Objective: 
    
    Create a polynomial hash for a string.

    s0an-1+s1an-2+…+sn-3a2+sn-2a+sn-1

    a is non-zero
    si is the ASCII value of the ith character in the string
    n is the length of the string

    Add the following strings:
        fist, sift, shift, fast, faster, shaft
        show their polynomial values
        also their hash values modulo 17 and 37
'''     

def ASCII_String_Hashing(string):
    str=string.split(', ') 
    # print(str)
    a=7
    arr=[0]*len(string)
    for i in range(len(str)):
        sum=0
        ij = 0
        for j in str[i]:
            k = ord(j)
            n = len(str[i])
            sum = sum + ( (a**(n-ij-1)) * k)
            
            print(k," * ",(a**(n-ij-1))," + ",end=' ')
            ij += 1
        # print(str[i],":",sum)
        print()
        arr[i] = sum
        print("0  ==> ",sum,"\n")

    hash1 = [None]*17
    hash2 = [None]*37

    for i in range(len(str)):
        pos_1 = arr[i]%17
        pos_2 = arr[i]%37

        while hash1[pos_1] != None:
            if hash1[pos_1] == None:
                break
            pos_1 += 1
            pos_1 %= 17
        hash1[pos_1] = str[i]

        while hash2[pos_2] != None:
            if hash2[pos_2] == None:
                break
            pos_2 += 1
            pos_2 %= 17
        hash2[pos_2] = str[i]


    return hash1 , hash2

mystr = 'fist, sift, shift, fast faster, shaft'
x,y = ASCII_String_Hashing(mystr)

print(x)
print()
print(y)

