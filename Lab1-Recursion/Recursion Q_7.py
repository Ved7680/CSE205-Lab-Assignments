"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Checking whether the string is palindrome or not using recursion. 
"""

def isPali(str):
    if len(str)<1:
        return True
    else:
        if str[0] == str[-1]:
            return isPali(str[1:-1])
        else:
            return False

print(isPali("MOM"))