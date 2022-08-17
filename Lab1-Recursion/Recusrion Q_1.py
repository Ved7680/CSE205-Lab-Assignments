"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Getting Factorial of a number using Recursion
"""

def factr(num):
    if num>=0 and num%1==0: # checks conditoin whether the number is poitive integer or not 
        if (num==0 or num==1):
            return 1
        else:
            return num*factr(num-1) # Recusrsion happens here
    else:
        print("!!Please Enter a Positive integer!!")

n = float(input("Enter a number: "))
print("Factorial of",n,":",factr(n)) # Printting of function
        
# I/O: 
# a.  0.5 ------> Enter a number: 0.5
#                 !!Please Enter a Positive integer!!
#                 Factorial of 0.5 : None

# b. 5 ------> Enter a number: 5
#              Factorial of 5.0 : 120.0