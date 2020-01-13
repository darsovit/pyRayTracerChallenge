#! python
#
#

from math import tan
from renderer.transformations import IdentityMatrix
from renderer.rays import Ray
from renderer.bolts import Point, Vector
from renderer.canvas import Canvas

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
        self.__transform = IdentityMatrix

    def HSize(self):
        return self.__hsize
    def VSize(self):
        return self.__vsize
    def GetFieldOfView(self):
        return self.__fov

    def Transform(self):
        return self.__transform
    def SetTransform(self, transform):
        self.__transform = transform

    def GetPixelSize(self):
        return self.__pixelSize

    def RayForPixel(self, x, y):
        xoffset = (x + 0.5) * self.GetPixelSize()
        yoffset = (y + 0.5) * self.GetPixelSize()
        world_x = self.__halfWidth - xoffset
        world_y = self.__halfHeight - yoffset
        transformInverse = self.Transform().Inverse()
        pixel = transformInverse.TimesTuple( Point(world_x, world_y, -1) )
        origin = transformInverse.TimesTuple( Point(0, 0, 0) )
        direction = (pixel - origin).normalize()
        directionV = Vector( direction[0], direction[1], direction[2] )
        return Ray(origin, directionV)

    def Render(self, world):
        canvas = Canvas( self.HSize(), self.VSize() )
        for y in range(self.VSize()):
            for x in range(self.HSize()):
                ray = self.RayForPixel(x, y)
                color = world.ColorAt( ray )
                canvas.SetPixel(x, y, color)
        return canvas