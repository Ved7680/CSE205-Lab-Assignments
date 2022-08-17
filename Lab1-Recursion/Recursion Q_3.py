"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Write a function addup() that accepts a number and adds up all the numbers from 0 to the number.
"""

def addup(num): # num must be positive integer
    if(num>=0):
        if num==0: # condition for num=0
            return 0
        else: # condition for num>=1
            return num+addup(num-1)

print("Sum: ",addup(int(input("Enter a number: "))))