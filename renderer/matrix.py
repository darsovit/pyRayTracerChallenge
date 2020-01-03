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

    def __str__(self):
        return '\n'.join(list(map(str, self.data)))

    def __getitem__(self,pos):
        return self.data[pos[0]][pos[1]]

    def Compare(self, rhs):
        EPSILON = 0.00001
        if len(rhs.data) != len(self.data):
            return False
        for i in range(len(self.data)):
            if len(self.data[i]) != len(rhs.data[i]):
                return False
            for j in range(len(self.data[i])):
                if not isclose(self.data[i][j], rhs.data[i][j], abs_tol=EPSILON):
                    return False
        return True


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

    def Transpose(self):
        newMatrixData = []
        rows = len(self.data)
        assert rows > 0
        cols = len(self.data[0])
        assert cols > 0
        for j in range(cols):
            newMatrixData += [[]]
        for i in range(rows):
            for j in range(cols):
                newMatrixData[j] += [self[i,j]]
        return Matrix(cols, rows, newMatrixData)
        
    def Determinant(self):
        det = 0
        if len(self.data) == 2 and len(self.data[0]) == 2:
            det = self[0,0]*self[1,1] - self[1,0]*self[0,1]
        else:
            for i in range(len(self.data)):
                det += self[0,i] * self.Cofactor(0,i)
        return det

    def Submatrix(self, row, column):
        newMatrixData = []
        for i in range(len(self.data)):
            if row == i:
                continue
            rowData = []
            for j in range(len(self.data[i])):
                if column == j:
                    continue
                rowData += [ self[i,j] ]
            newMatrixData += [ rowData ]
        return Matrix(len(newMatrixData),len(newMatrixData[0]),newMatrixData)
        
    def Minor(self, row, column):
        return self.Submatrix(row,column).Determinant()

    def Cofactor(self, row, column):
        determinant = self.Submatrix(row,column).Determinant()
        negate = -1 if (row + column) % 2 == 1 else 1
        return determinant * negate

    def IsInvertible(self):
        return self.Determinant() != 0

    def Inverse(self):
        determinant = self.Determinant()
        if 0 == determinant:
            raise NotInvertibleError
        newMatrixData = []
        rows = len(self.data)
        assert rows > 0
        cols = len(self.data[0])
        assert cols > 0
        for j in range(cols):
            newMatrixData += [[]]
        for i in range(rows):
            for j in range(cols):
                cofactor = self.Cofactor(i,j)
                newMatrixData[j] += [ cofactor / determinant ]
        return Matrix(cols,rows,newMatrixData)

IdentityMatrix = Matrix(4,4,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])