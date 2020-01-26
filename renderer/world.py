#! python
#

from renderer.bolts import Color, IdentifyHit, Vector
from renderer.rays import Ray

from math import isclose, sqrt

class World:
    def __init__(self, objects=[], lights=[]):
        self.__objects = objects
        self.__lights  = lights

    def NumObjects(self):
        return len(self.__objects)

    def NumLights(self):
        return len(self.__lights)

    def SetLight(self, light):
        self.__lights = [ light ]

    def Lights(self):
        return self.__lights

    def Objects(self):
        return self.__objects

    def AddObject(self, object):
        self.__objects += [ object ]

    def Intersects(self, ray):
        intersections = []
        for object in self.Objects():
            intersections += object.Intersect( ray )
        intersections.sort(key=lambda x: x['time'])
        return intersections

    def ShadeHit(self, computation, remaining=5):
        shadowed = self.IsShadowed(computation['over_point'])
        material = computation['object'].Material()
        surface = material.Lighting(self.Lights()[0], computation['over_point'], computation['eyev'], computation['normalv'], shadowed, computation['object'].TransformInverse())
        reflected = self.ReflectedColorAt(computation, remaining)
        refracted = self.RefractedColorAt(computation, remaining)
        color = Color(0,0,0)
        if material.Reflectivity() > 0 and material.Transparency() > 0:
            assert 'reflectance' in computation
            reflectance = computation['reflectance']
            color = surface + reflected * reflectance + refracted * (1 - reflectance)
        else:
            color = surface + reflected + refracted
        return Color(color[0], color[1], color[2] )

    def ColorAt(self, ray, remaining=5):
        intersections = self.Intersects( ray )
        hit = IdentifyHit( intersections )
        if not hit:
            return Color( 0, 0, 0 )
        else:
            return self.ShadeHit(hit['object'].PrepareComputations(ray, hit['time']), remaining)

    def ReflectedColorAt(self, computation, remaining):
        reflectivity = computation['object'].Material().Reflectivity()
        if isclose(reflectivity, 0.0) or remaining < 1:
            return Color( 0, 0, 0 )
        else:
            return self.ColorAt(Ray(computation['over_point'], computation['reflectv']), remaining-1)*reflectivity

    def RefractedColorAt(self, computation, remaining):
        if isclose(computation['object'].Material().Transparency(), 0) or remaining < 1:
            return Color(0, 0, 0)
        else:
            cosI   = 0
            nRatio = 0
            sin2_t = 0
            if 'sin2_t' not in computation:
                nRatio = computation['n1'] / computation['n2']
                cosI   = computation['eyev'].dot(computation['normalv'])
                sin2_t = (nRatio * nRatio) * ( 1 - (cosI * cosI) )
            else:
                nRatio = computation['nRatio']
                sin2_t = computation['sin2_t']
                cosI   = computation['cosI']
            if sin2_t > 1:
                return Color(0, 0, 0)
            cos_t = sqrt(1.0 - sin2_t)
            direction = computation['normalv'] * (nRatio * cosI - cos_t) - computation['eyev'] * nRatio
            refractRay = Ray( computation['under_point'], Vector(direction[0], direction[1], direction[2]) )
            colorTuple = self.ColorAt( refractRay, remaining-1 ) * computation['object'].Material().Transparency()
            return Color( colorTuple[0], colorTuple[1], colorTuple[2] )

    def IsShadowed(self, point):
        vectorTowardLight = (self.Lights()[0].Position() - point)
        distance = vectorTowardLight.magnitude()
        rayToLight = Ray( point, vectorTowardLight.normalize() )
        intersections = self.Intersects( rayToLight )
        hit = IdentifyHit( intersections )
        if hit and hit['time'] < distance:
            return True
        else:
            return False
        
        