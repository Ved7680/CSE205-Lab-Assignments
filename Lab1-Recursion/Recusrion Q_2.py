"""
    AUTHOR: Ved J Nayi
    DOC: 04-08-22
    Objective: Experimenting how recusrion works
"""

def first():
    second()
    print("I am first")

def second():
    third()
    print("I am second")

def third():
    fourth()
    print("I am third")

def fourth():
    print("I am fourth")

print("Fourth Function: ")
fo = fourth()

print("Third Function: ")
th = third()

print("Second Function: ")
sec = second()

print("First Function: ")
fi = first()

# Write a function addup() that accepts a number and adds up all the numbers from 0 to the number.