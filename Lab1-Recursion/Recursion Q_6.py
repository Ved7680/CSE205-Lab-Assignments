"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: getting HCF of two numbers using recusrion
"""

def HCF(num1,num2):
    rem = num1%num2
    if rem == 0:
        return num2
    else:
        return HCF(rem,num1)

ans = HCF(10,3)
print(ans)
            