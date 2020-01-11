#! python
#
#

from renderer.matrix import IdentityMatrix
from math import sqrt
from renderer.bolts import Point, Vector
from renderer.material import Material

class Sphere:
    
    def __init__(self, transform=IdentityMatrix, material=Material()):
        self.__transform = transform
        self.__material  = material

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
        return self.__transform

    def SetTransform(self, transform):
        self.__transform = transform

    def Normal(self, position):
        object_point = self.Transform().Inverse().TimesTuple(position)
        object_normal = object_point - Point(0,0,0)
        world_normal  = self.Transform().Inverse().Transpose().TimesTuple(object_normal)
        world_normal  = Vector( world_normal[0], world_normal[1], world_normal[2] )
        return world_normal.normalize()

    def PrepareComputations(self, ray, time):
        computations = {}
        computations['time'] = time
        computations['object'] = self
        computations['point']  = ray.Position(time)
        computations['eyev']   = -ray.Direction().normalize()
        computations['normalv'] = self.Normal( computations['point'] )
        return computations

    def Material(self):
        return self.__material

    def SetMaterial(self, material):
        self.__material = material

    def __str__(self):
        return ' '.join(list(map(str, ['Sphere:{', 'Material:', self.Material(), 'Transform:', self.Transform(), '}'])))

    def __eq__(self, rhs):
        return self.Material() == rhs.Material() and self.Transform() == rhs.Transform()