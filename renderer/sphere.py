#! python
#
#

from renderer.matrix import IdentityMatrix
from math import sqrt
from renderer.bolts import Point, Vector
from renderer.material import Material
from renderer.shape import Shape

class Sphere(Shape):

    def LocalIntersect(self, localRay):
        sphereToRay = localRay.Origin() - Point(0,0,0)
        a = localRay.Direction().dot( localRay.Direction() )
        b = 2 * localRay.Direction().dot( sphereToRay )
        c = sphereToRay.dot( sphereToRay ) - 1
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return ()
        t1 = ( -b - sqrt(discriminant) ) / (2 * a)
        t2 = ( -b + sqrt(discriminant) ) / (2 * a)
        return [{'time':t1, 'object':self}, {'time':t2, 'object':self}]


    def LocalNormal(self, objectPoint):
        objectNormal = objectPoint - Point(0,0,0)
        return Vector(objectNormal[0], objectNormal[1], objectNormal[2])


    def __str__(self):
        return ' '.join(list(map(str, ['Sphere:{', 'Material:', self.Material(), 'Transform:', self.Transform(), '}'])))

    def __eq__(self, rhs):
        return self.Material() == rhs.Material() and self.Transform() == rhs.Transform()