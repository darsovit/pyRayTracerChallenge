#! python
#

from renderer.bolts import Color, IdentifyHit
from renderer.rays import Ray

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

    def ShadeHit(self, computation):
        return computation['object'].Material().Lighting(self.Lights()[0], computation['over_point'], computation['eyev'], computation['normalv'], self.IsShadowed(computation['over_point']), computation['object'].TransformInverse())

    def ColorAt(self, ray):
        intersections = self.Intersects( ray )
        hit = IdentifyHit( intersections )
        if not hit:
            return Color( 0, 0, 0 )
        else:
            return self.ShadeHit(hit['object'].PrepareComputations(ray, hit['time']))

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
        
        