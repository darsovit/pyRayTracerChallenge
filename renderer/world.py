#! python
#

from renderer.bolts import Color, IdentifyHit
from renderer.rays import Ray
from math import isclose

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
        surface = computation['object'].Material().Lighting(self.Lights()[0], computation['over_point'], computation['eyev'], computation['normalv'], shadowed, computation['object'].TransformInverse())
        reflected = self.ReflectedColorAt(computation, remaining)
        return surface + reflected

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
        
        