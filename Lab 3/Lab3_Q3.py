'''
    AUTHOR: Ved J Nayi
    DOC: 01-09-22
    Objective: Declaring a class Array2D and performing the funtions listed below:
                
    Matrix( rows, ncols ): Creates a new matrix containing nrows and ncols with each element initialized to 0.

    numRows( ): Returns the number of rows in the matrix.

    numCols( ): Returns the number of columns in the matrix.

    getitem ( row, col ): Returns the value stored in the given matrix element. Both row and col must be within the valid range.

    setitem ( row, col, scalar ): Sets the matrix element at the given row and col to scalar. The element indices must be within the valid range.

    scaleBy( scalar ): Multiplies each element of the matrix by the given scalar value. The matrix is modified by this operation.

    transpose( ): Returns a new matrix that is the transpose of this matrix.

    add ( rhsMatrix ): Creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of the two matrices must be the same.

    subtract ( rhsMatrix ): The same as the add() operation but subtracts the two matrices.

    multiply ( rhsMatrix ): Creates and returns a new matrix that is the result of multiplying this matrix to the given rhsMatrix. The two matrices must be of appropriate sizes as defined for matrix multiplication.
'''

class Array2D:
    def __init__(self,rows,cols):
        self.my2darr = [[0]*cols for i in range(rows)]

    def numRows(self): # For gettting number of rows from the array
        return len(self.my2darr)

    def numCols(self): # for getting number of columns from array
        return len(self.my2darr[0])

    def getItem(self,r,c):
        return self.my2darr[r][c]
    
    def setItem(self,r,c,value):
        self.my2darr[r][c] = value
        return self.my2darr

    def Matrix(self,rows,cols): # For making a array where each element is initialized to 0
        assert rows==self.numRows() and cols == self.numCols(), "Given parameters does not match the size of matrix!"
        print("Enter elements of the matrix:")
        for i in range(rows):
            for j in range(cols):
                n = int(input())
                self.my2darr[i][j] = n

    def disp2D(self): # For diaplaying the array
        for i in range(len(self.my2darr)):
            for j in range(len(self.my2darr[0])):
                print(self.my2darr[i][j], end= ' ')
            print()

    def generateSparseMatrix(self):
        c=0
        for i in range(len(self.my2darr)):
            for j in range(len(self.my2darr[0])):
                if self.my2darr[i][j] != 0:
                    c+=1

        res = Array2D(c,3)
        r=0
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if(self.my2darr[i][j]!=0):
                    t = self.getItem(i,j)
                    res.my2darr[r][0] = i
                    res.my2darr[r][1]=j
                    res.my2darr[r][2]=t
                    r+=1
        return res

    def SparseSetItem(self,x,y,value):
        assert x<len(self.my2darr) and y<len(self.my2darr[0]) and x>=0 and y>=0, "Index value out of bounds" 
        if value == 0:
            res = Array2D(self.numOfRows()-1,self.numOfCols())
            c=0
            flag = 0
            for i in range(len(self.my2darr)):
                for j in range(len(self.my2darr[0])):
                    if self.my2darr[c][0] == x and self.my2darr[c][1] == y:
                        flag = 1
                        c+=1
                        continue
                    else:
                        if flag == 1:
                            res.my2darr[c-1] = self.my2darr[c]
                        else:
                            res.my2darr[c] = self.my2darr[c]
                        
                return res
        else:
            for i in range(self.my2darr):
                res = Array2D(self.numOfRows()-1,self.numOfCols())
                if(res.my2darr[i][0]==x and res.my2darr[i][1]==y):
                    res.my2darr[i][2]=value
            return res  
    
    def SparsegetItem(self,x,y):
        assert x<len(self.my2darr) and y<len(self.my2darr[0]) and x>=0 and y>=0, "Index value out of bounds"
        for i in range(self.numOfRows()):
            if(self.my2darr[i][0]==x and self.my2darr[i][1]==y):
                return self.my2darr[i][2]

    def getRank(self):
        return (self.numCols(),self.numCols())

    def SparseClear(self,value):
        for i in range(self.numRows()):
            self.my2darr[i][2] = value
    
    def SparseScaleBy(self,value):
        for i in range(self.numRows()):
            self.my2darr[i][2] = self.my2darr[i][2]*value

    def SparseTranspose(self):
        res = Array2D(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            res.my2darr[i][0] = self.my2darr[i][1]
            res.my2darr[i][1] = self.my2darr[i][0]
            res.my2darr[i][2] = self.my2darr[i][2]
        return res

    def SparseAdd(self,m1):
        assert self.getRank() == m1.getRank(), "Trying to add matrices of various sizes!"
        res = Array2D(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numRows()):
                if(self.my2darr[i][0]==m1.my2darr[j][0] and self.my2darr[i][1]==m1.my2darr[j][1]):
                    res.my2darr[i][1] = self.my2darr[i][1]
                    res.my2darr[i][0] = self.my2darr[i][0]
                    res.my2darr[i][2] = self.my2darr[i][2]+m1.my2darr[j][2]
        return res
    
    def SparseSub(self,m1):
        assert self.getRank() == m1.getRank(), "Trying to subtract matrices of various sizes!"
        res = Array2D(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numRows()):
                if(self.my2darr[i][0]==m1.my2darr[j][0] and self.my2darr[i][1]==m1.my2darr[j][1]):
                    res.my2darr[i][1] = self.my2darr[i][1]
                    res.my2darr[i][0] = self.my2darr[i][0]
                    res.my2darr[i][2] = self.my2darr[i][2]-m1.my2darr[j][2]
        return res


    def SparseMultiply(self,m1):
        assert self.getRank() == m1.getRank(), "Trying to Multiply  Sparsematrices of various sizes!"
        res = Array2D(self.numRows(),self.numCols())
        m1 = m1.SparseTranspose()
        for i in range(self.numRows()):
            res.my2darr[i][2]=0
            for j in range(m1.numRows()):
                if(self.my2darr[i][1]==m1.my2darr[j][1]):
                    res.my2darr[i][0] = self.my2darr[i][0]
                    res.my2darr[i][1] = m1.my2darr[j][0]
                    res.my2darr[i][2] = res.my2darr[i][2]+self.my2darr[i][2]*m1.my2darr[j][2]
                
        return res

m = Array2D(2,2)
m.setItem(0,0,1)
m.setItem(0,1,2)
m.setItem(1,0,3)
m.setItem(1,1,0)
res = m.generateSparseMatrix()
res.disp2D()
print()
rest = res.SparseTranspose()

rest.disp2D()
print()
resm = res.SparseMultiply(rest)

resm.disp2D()