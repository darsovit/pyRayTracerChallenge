#! python
#
#

from renderer.matrix import Matrix, IdentityMatrix
from math import cos,sin
from renderer.bolts import Vector

def Translation(x, y, z):
    return Matrix(4,4,[[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])

def Scaling(x, y, z):
    return Matrix(4,4,[[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])

def Rotation_x( radian ):
    return Matrix(4,4,[[1,0,0,0],[0,cos(radian),-sin(radian),0],[0,sin(radian),cos(radian),0],[0,0,0,1]])

def Rotation_y( radian ):
    return Matrix(4,4,[[cos(radian),0,sin(radian),0],[0,1,0,0],[-sin(radian),0,cos(radian),0],[0,0,0,1]])

def Rotation_z( radian ):
    return Matrix(4,4,[[cos(radian),-sin(radian),0,0],[sin(radian),cos(radian),0,0],[0,0,1,0],[0,0,0,1]])

def Shearing( x_y, x_z, y_x, y_z, z_x, z_y ):
    return Matrix(4,4,[[1,x_y,x_z,0],[y_x,1,y_z,0],[z_x,z_y,1,0],[0,0,0,1]])

def ViewTransform( fromPoint, toPoint, upVector ):
    forward = ( toPoint - fromPoint ).normalize()
    assert forward[3] == 0
    forwardV = Vector( forward[0], forward[1], forward[2] )
    leftV = forwardV.cross( upVector.normalize() )
    trueUpV = leftV.cross( forwardV )
    orientation = Matrix( 4, 4, [[leftV[0], leftV[1], leftV[2], 0],
                          [trueUpV[0], trueUpV[1], trueUpV[2], 0],
                          [-forwardV[0], -forwardV[1], -forwardV[2], 0],
                          [0, 0, 0, 1]] )
    return orientation * Translation( -fromPoint[0], -fromPoint[1], -fromPoint[2] )
