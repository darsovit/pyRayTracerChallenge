#!python
#
#
from renderer.material import Material
from renderer.transformations import IdentityMatrix
from renderer.bolts import Vector, EPSILON

class Shape:
    def __init__(self, transform=IdentityMatrix, material=Material()):
        self.SetTransform(transform)
        self.__material  = material

    def Material(self):
        return self.__material

    def Transform(self):
        return self.__transform
    def TransformInverse(self):
        return self.__transformInverse
    def TransformInverseTranspose(self):
        return self.__transformInverseTranspose

    def SetTransform(self, transform):
        self.__transform = transform
        self.__transformInverse = self.Transform().Inverse()
        self.__transformInverseTranspose = self.TransformInverse().Transpose()

    def SetMaterial(self, material):
        self.__material = material

    def Intersect(self, ray):
        localRay = ray.Transform( self.TransformInverse() )
        return self.LocalIntersect( localRay )

    def Normal(self, point):
        localPoint = self.TransformInverse().TimesTuple( point )
        localNormal = self.LocalNormal( localPoint )
        tempWorldNormal = self.TransformInverseTranspose().TimesTuple( localNormal )
        worldNormal = Vector( tempWorldNormal[0], tempWorldNormal[1], tempWorldNormal[2] )
        return worldNormal.normalize()

    def PrepareComputations(self, ray, time):
        computations = {}
        computations['time'] = time
        computations['object'] = self
        computations['point']  = ray.Position(time)
        computations['eyev']   = -ray.Direction().normalize()
        computations['normalv'] = self.Normal( computations['point'] )
        computations['inside'] = 0 > computations['normalv'].dot(computations['eyev'])
        if computations['inside']:
            computations['normalv'] = -computations['normalv']
        computations['over_point'] = computations['point'] + computations['normalv'] * EPSILON
        return computations
