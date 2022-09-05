'''
    AUTHOR: Ved J Nayi
    DOC: 01-09-22
    Objective: Declaring and class Array2D and performing the operations given below
'''

class Array2D:

    def __init__(self):
        self.my2darr = list(list())

    def Array2D(self,rows,cols): # for setting the array to None
        self.my2darr = [[None for _ in range(cols)] for _ in range(rows)]
        return self.my2darr

    def disp2D(self): # For diaplaying the array
        for i in range(len(self.my2darr)):
            for j in range(len(self.my2darr[0])):
                print(self.my2darr[i][j], end= ' ')
            print()

    def numRows(self): # For gettting number of rows from the array
        return len(self.my2darr)

    def numCols(self): # for getting number of columns from array
        return len(self.my2darr[0])

    def clear(self,value): # For setting all the values in the column to a specific value
        self.my2darr = [[value for _ in range(len(self.my2darr[0]))] for _ in range(len(self.my2darr))]
        return self.my2darr

    def getItem(self,i1,i2): # For getting an element from a specific position of a matrix
        if i1<len(self.my2darr) and i2<len(self.my2darr[0]):
            return self.my2darr[i1][i2]
        else:
            print("Position of element is not valid")

    def setItem(self,i1,i2,value): # For setting a specific element of a matrix to a given value
        if i1<len(self.my2darr) and i2<len(self.my2darr[0]):
            self.my2darr[i1][i2] = value
            return self.my2darr
        else:
            print("Position of element is not valid")



my2d = Array2D()

my2d.Array2D(3,3)

my2d.disp2D()
print()
print("Rows:",my2d.numRows())
print("Cols:",my2d.numCols())
print()
my2d.clear(1)
my2d.disp2D()
print()
print(my2d.getItem(0,3))
print()
my2d.setItem(0,1,0)
my2d.disp2D()



