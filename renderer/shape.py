#!python
#
#
from renderer.material import Material
from renderer.transformations import IdentityMatrix
from renderer.bolts import Vector, EPSILON
from renderer.rays import Ray
from math import sqrt

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

    def PrepareComputations(self, ray, time, intersections=[]):
        computations = {}
        computations['time'] = time
        computations['object'] = self
        computations['point']  = ray.Position(time)
        computations['eyev']   = -ray.Direction().normalize()
        computations['normalv'] = self.Normal( computations['point'] )
        computations['inside'] = 0 > computations['normalv'].dot(computations['eyev'])
        if computations['inside']:
            computations['normalv'] = -computations['normalv']
        computations['over_point'] = computations['point'] + ( computations['normalv'] * EPSILON )
        computations['under_point'] = computations['point'] - ( computations['normalv'] * EPSILON )
        computations['reflectv'] = ray.Direction().reflect( computations['normalv'] )
        containers = []
        
        for intersection in intersections:
            if time == intersection['time']:
                if len(containers) == 0:
                    computations['n1'] = 1.0
                else:
                    computations['n1'] = containers[-1].Material().RefractiveIndex()
            if intersection['object'] in containers:
                containers.remove(intersection['object'])
            else:
                containers.append( intersection['object'] )
            if time == intersection['time']:
                if len(containers) == 0:
                    computations['n2'] = 1.0
                else:
                    computations['n2'] = containers[-1].Material().RefractiveIndex()

        if self.Material().Transparency() > 0:
            cos = computations['eyev'].dot( computations['normalv'] )
            computations['cosI'] = cos
            if computations['n1'] > computations['n2']:
                nRatio = computations['n1'] / computations['n2']
                computations['nRatio'] = nRatio
                computations['sin2_t'] = (nRatio*nRatio) * (1.0 - (cos * cos) )
                if computations['sin2_t'] > 1.0:
                    computations['reflectance'] = 1.0
                else:
                    cos_t = sqrt(1.0 - computations['sin2_t'])
                    cos = cos_t
            if 'reflectance' not in computations:
                r0 = pow((computations['n1'] - computations['n2']) / (computations['n1'] + computations['n2']), 2)
                computations['reflectance'] = r0 + (1 - r0) * pow((1-cos),5)
        return computations
