#! python
#
#

from renderer.matrix import Matrix
from math import cos,sin

def Translation(x, y, z):
    return Matrix(4,4,[[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])

def Scaling(x, y, z):
    return Matrix(4,4,[[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])

def Rotation_x( radian ):
    return Matrix(4,4,[[1,0,0,0],[0,cos(radian),-sin(radian),0],[0,sin(radian),cos(radian),0],[0,0,0,1]])