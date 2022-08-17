"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Function reverse() that accepts a string and reverse it
"""

def reverse(str):
    if len(str)==0:
        return

    temp = str[0] 
    reverse(str[1:])
    print(temp, end='')   
    

reverse("My Name is Ved")