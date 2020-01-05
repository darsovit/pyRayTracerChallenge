#! python
#
#

from math import sqrt
from renderer.bolts import Point

class Sphere:
    def __init__(self):
        pass

    def Intersect(self, ray):
        sphereToRay = ray.Origin() - Point(0,0,0)
        a = ray.Direction().dot( ray.Direction() )
        b = 2 * ray.Direction().dot( sphereToRay )
        c = sphereToRay.dot( sphereToRay ) - 1
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return ()
        t1 = ( -b - sqrt(discriminant) ) / (2 * a)
        t2 = ( -b + sqrt(discriminant) ) / (2 * a)
        return [t1, t2]