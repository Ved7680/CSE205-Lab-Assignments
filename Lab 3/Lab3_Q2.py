
class Array2D():
    def __init__(self,Rows,Cols):
        self.my2darr = [[None]*Cols for i in range(Rows)]

    def numOfRows(self):
        return len(self.my2darr)

    def numOfCols(self):
        return len(self.my2darr[0])

    def printArray(self):
        for i in range(len(self.my2darr)):
            for j in range(len(self.my2darr[0])):
                print(self.my2darr[i][j],end=" ")
            print()

    def clear(self,value):
        self.my2darr = [[value]*len(self.my2darr[0]) for i in range(len(self.my2darr))]

    def getItem(self,x,y):
        assert x<len(self.my2darr) and y<len(self.my2darr[0]) and x>=0 and y>=0, "Index value out of bounds" 
        for i in range(len(self.my2darr)):
            for j in range(len(self.my2darr[0])):
                if(i==x and j==y):
                    return self.my2darr[i][j]

    def setItem(self,x,y,value):
        assert x<len(self.my2darr) and y<len(self.my2darr[0]) and x>=0 and y>=0, "Index value out of bounds"
        for i in range(self.numOfRows()):
            for j in range(self.numOfCols()):
                if(i==x and j==y):
                    self.my2darr[i][j] = value
                    return
    
    def generateSparseArray(self):
        c=0
        for i in range(self.numOfRows()):
            for j in range(self.numOfCols()):
                if(self.my2darr[i][j]!=0):
                    c+=1
        res = Array2D(c,3)
        r=0
        for i in range(self.numOfRows()):
            for j in range(self.numOfCols()):
                if(self.my2darr[i][j]!=0):
                    t = self.getItem(i,j)
                    res.my2darr[r][0] = i
                    res.my2darr[r][1]=j
                    res.my2darr[r][2]=t
                    r+=1
        return res
    
m = Array2D(4,6)
m.clear(0)
m.setItem(3,4,5)
m1 = m.generateSparseArray()
m1.printArray()