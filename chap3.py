#! python
#
# Chapter 3 Exercises

from renderer.matrix import Matrix, IdentityMatrix
from renderer.bolts  import Tuple
def Question1():
    print( "Identity Matrix" )
    print( IdentityMatrix )
    print( "Inverted Identity Matrix" )
    print( IdentityMatrix.Inverse() )

def Question2():
    A = Matrix(4,4,[[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,-1]])
    invertA = A.Inverse()
    print('A')
    print(A)
    print('A.Inverse()')
    print(invertA)
    print('A * A.Inverse()')
    print(A * invertA)

def Question3():
    A = Matrix(4,4,[[-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]])
    inverseTransposeA = A.Transpose().Inverse()
    transposeInverseA = A.Inverse().Transpose()
    print('A:\n{}'.format(A))
    print('A.Transpose().Inverse():\n{}'.format(inverseTransposeA))
    print('A.Inverse().Transpose():\n{}'.format(transposeInverseA))

def Question4():
    IdentityButY = Matrix(4,4,[[1,0,0,0],[0,10,0,0],[0,0,1,0],[0,0,0,1]])
    tuple        = Tuple(1,1,1,1)
    print('Tuple:', tuple)
    print('IdentityButY * Tuple:', IdentityButY.TimesTuple(tuple))

Question1()
Question2()
Question3()
Question4()