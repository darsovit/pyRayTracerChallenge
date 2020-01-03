#! python
#
#

from renderer.matrix import Matrix

def Translation(x, y, z):
    return Matrix(4,4,[[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])