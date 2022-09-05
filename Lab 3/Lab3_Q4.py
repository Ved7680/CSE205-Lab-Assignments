'''
    AUTHOR: Ved J Nayi
    DOC: 05-09-22
    Objective: Making Game of Life
'''

class LifeGrid():
    def __init__(self,nrows,nCols):
        self.Rows = [[0]*nCols for i in range(nrows)]
    
    def numRows(self):
        return len(self.Rows)
    
    def numCols(self):
        return len(self.Rows[0])

    def clearCell(self,x,y):
        assert x>=0 and x<self.numRows() and y>=0 and y<self.numCols(), "Enter valid range of indices"
        self.Rows[x][y]= 0
        return
    
    def setCell(self,x,y):
        assert x>=0 and x<self.numRows() and y>=0 and y<self.numCols(), "Enter valid range of indices"
        self.Rows[x][y]=1
        return

    def isLiveCell(self,x,y):
        assert x>=0 and x<self.numRows() and y>=0 and y<self.numCols(), "Enter valid range of indices"
        return (self.Rows[x][y]==1)
    
    def configure(self,l):
        for i in l:
            assert(len(i)==2), "Invalid argument"
            x = i[0]
            y = i[1]
            assert x>=0 and x<self.numRows() and y>=0 and y<self.numCols(), "Enter valid range of indices"
            self.Rows[x][y]=1
                
    def numLiveNeighbor(self,x,y):
        assert x>=0 and x<self.numRows() and y>=0 and y<self.numCols(), "Enter valid range of indices"
        c=0
        l = [-1,1]
        for i in l:
            t1 = x-i
            t2 = y-i
            if(self.Rows[t1][t2]==1 and t1>=0 and t1<self.numRows() and t2>=0 and t2<self.numCols()):
                c+=1
        for i in l:
            t1 = x-i
            t2 = y
            if(self.Rows[t1][t2]==1 and t1>=0 and t1<self.numRows() and t2>=0 and t2<self.numCols()):
                c+=1
        for i in l:
            t1 = x
            t2 = y-i
            if(self.Rows[t1][t2]==1 and t1>=0 and t1<self.numRows() and t2>=0 and t2<self.numCols()):
                c+=1
        
        for i in l:
            t1 = x - i
            t2 = y + i
            if(self.Rows[t1][t2]==1 and t1>=0 and t1<self.numRows() and t2>=0 and t2<self.numCols()):
                c+=1
        
        return c

    def showGrid(self):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print(self.Rows[i][j],end=" ")
            print()

m = LifeGrid(3,3)
m.showGrid()
l = [(0,0),(1,1),(2,2)]
m.configure(l)
print()
m.showGrid()
print()
m.setCell(0,1)
m.showGrid()
print()
print("Number of Live Neighbours:",m.numLiveNeighbor(1,1))