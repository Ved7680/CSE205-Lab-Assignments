"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Printing a specific number in fibonacci series
"""

def Fibo(num):
    if num>0:
        if(num==1):
            return 0
        elif(num==2):
            return 1
        elif (num>2):
            return Fibo(num-1)+Fibo(num-2)
    else:
        print("!!Enter a poistive number!!")

n = int(input("Enter a number: "))
ans = Fibo(n)
print(n,"th number of Fibonacci Series:",ans)
    
    