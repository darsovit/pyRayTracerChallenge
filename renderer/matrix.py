#! python
#
# Matrix class data

from math import isclose
from renderer.bolts import Tuple

class Matrix:
    def __init__(self,rows,cols,data):
        self.data = data
        assert len(self.data) == rows, 'Expected num rows {} not equal to num rows {}'.format(rows,len(self.data))
        for i in range(len(self.data)):
            assert len(self.data[i]) == cols, 'Expected size of cols {} is not equal to size of cols {}'.format(cols,len(self.data[0]))
    
    def __getitem__(self,pos):
        return self.data[pos[0]][pos[1]]
        
    def __eq__(self,rhs):
        if len(rhs.data) != len(self.data):
            return False
        for i in range(len(self.data)):
            if len(self.data[i]) != len(rhs.data[i]):
                return False
            for j in range(len(self.data[i])):
                if not isclose(self.data[i][j], rhs.data[i][j]):
                    return False
        return True

    def __mul__(self,rhs):
        vals = []
        for x in range(len(rhs.data)):
            rowdata = []
            for y in range(len(rhs.data[x])):
                base = Tuple( self[x,0],self[x,1],self[x,2],self[x,3] )
                rowdata += [base.dot( Tuple(rhs[0,y],rhs[1,y],rhs[2,y],rhs[3,y]) )]
            vals += [rowdata]
        return Matrix(len(rhs.data),len(rhs.data[0]),vals)

    def TimesTuple(self,tuple):
        tupleMatrixData = []
        for i in range(len(tuple.val)):
            rowData = [ tuple[i] ]
            tupleMatrixData += [ rowData ]
        tupleMatrix = Matrix(len(tuple.val),1,tupleMatrixData)
        resultMatrix = self * tupleMatrix
        resultTupleData = []
        for i in range(len(resultMatrix.data)):
            resultTupleData += [ resultMatrix[i,0] ]
        w = 0
        z = 0
        y = 0
        x = 0
        if len(resultTupleData) > 3:
            w = resultTupleData[3]
        if len(resultTupleData) > 2:
            z = resultTupleData[2]
        if len(resultTupleData) > 1:
            y = resultTupleData[1]
        if len(resultTupleData) > 0:
            x = resultTupleData[0]
        return Tuple( x, y, z, w )