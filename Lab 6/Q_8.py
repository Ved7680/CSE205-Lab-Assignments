'''
    AUTHOR: Ved J Nayi - AU2140055
    DOC: 25-10-22
    Objective: 
    
    Assigning jobs to servers.

    There are 17 servers numbered 0..16.
    The students of CSE205 with roll numbers from 1 to 126 are assigned to these servers using a modulo 17 hashing strategy (roll_no % 17).
    The students starts working on their assigned servers. After some time, 4 servers crash, and we are left with 13 servers.

    Now, we need to rehash. Such a rehash would typically require every student to be reassigned to a new server.

        (a) Come up with a strategy (algorithm) such that least number of students are affected by the crash.

        (b) The reassigned students should be spread as fairly as possible across the remaining servers
'''   
import random


def Hashing_2D(arr,size):

    hash = [[0]*1 for _ in range(size)]
    # print(hash)

    for i in range(len(arr)):
        m = arr[i]%size
        hash[m].append(arr[i])
    
    return ([k[1:] for k in (hash[0:])])

def Reassign_Hash(hash,crash_server):
    crashed = []
    for i in crash_server:
        crashed.append(hash[i])
    
    final_hash = []
    for i in range(17):
        if i in crash_server:
            final_hash.append(None)
        else:
            final_hash.append([])
    
    for i in range(1,127):
        pos = i%17
        if final_hash[pos]!=None:
            final_hash[pos].append(i)

    for i in crashed:
        count=1
        # Using Double Hashing, m=17(before crashing) , p=13(after crashing)
        for j in i:
            pos = j%17

            new_pos = ( pos+count*(1 + (pos%13)) )%17

            if final_hash[new_pos]!=None:
                final_hash[new_pos].append(j)
                count+=1
                new_pos = ( pos+count*(1 + (pos%13)) )%17
            else:
                count+=1
                new_pos = ( pos+count*(1 + (pos%13)) )%17
    
    return final_hash


arr = [1]*126
for i in range(1,126):
    arr[i] = i+1

mylist = Hashing_2D(arr,17)

a = random.randrange(0,17)
b = random.randrange(0,17)
c = random.randrange(0,17)
d = random.randrange(0,17)

if (a!=b!=c!=d):
    crash = [a,b,c,d]
    print(Reassign_Hash(mylist,crash))