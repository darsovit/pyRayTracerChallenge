#! python
#
#

from renderer.transformations import IdentityMatrix
from math import tan

class Camera:
    def __init__(self, hsize, vsize, fov):
        self.__hsize = hsize
        self.__vsize = vsize
        self.__fov   = fov
        halfView = tan(fov/2)
        aspect   = hsize / vsize
        if aspect >= 1:
            self.__halfWidth = halfView
            self.__halfHeight = halfView / aspect
        else:
            self.__halfHeight = halfView
            self.__halfWidth  = halfView * aspect
        self.__pixelSize = (2*self.__halfWidth) / hsize

    def HSize(self):
        return self.__hsize
    def VSize(self):
        return self.__vsize
    def GetFieldOfView(self):
        return self.__fov

    def Transform(self):
        return IdentityMatrix

    def GetPixelSize(self):
        return self.__pixelSize