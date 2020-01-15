#! python
#
#

from renderer.shape import Shape
from renderer.bolts import Vector, EPSILON

class Plane(Shape):
    def LocalNormal( self, localPoint ):
        return Vector( 0, 1, 0 )

    def LocalIntersect(self, localRay):
        if abs(localRay.Direction()[1]) < EPSILON:
            return []
        timeToIntersect = (0 - localRay.Origin()[1])/ localRay.Direction()[1]
        return [{'time': timeToIntersect, 'object':self}]
