#! python
#
#

from renderer.matrix import IdentityMatrix
from math import sqrt
from renderer.bolts import Point

class Sphere:
    def __init__(self):
        self.transform = IdentityMatrix

    def Intersect(self, ray):
        transformedRay = ray.Transform( self.Transform().Inverse() )
        sphereToRay = transformedRay.Origin() - Point(0,0,0)
        a = transformedRay.Direction().dot( transformedRay.Direction() )
        b = 2 * transformedRay.Direction().dot( sphereToRay )
        c = sphereToRay.dot( sphereToRay ) - 1
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return ()
        t1 = ( -b - sqrt(discriminant) ) / (2 * a)
        t2 = ( -b + sqrt(discriminant) ) / (2 * a)
        return [{'time':t1, 'object':self}, {'time':t2, 'object':self}]

    def Transform(self):
        return self.transform

    def SetTransform(self, transform):
        self.transform = transform