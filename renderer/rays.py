#! python
#
#
from math import isclose
from renderer.bolts import Point, Vector
class Ray:
    def __init__(self, origin, direction):
        assert origin.isPoint()
        assert direction.isVector()
        self.__origin = origin
        self.__direction = direction

    def Origin(self):
        return self.__origin

    def Direction(self):
        return self.__direction

    def Position(self, time):
        return self.Origin() + ( self.Direction() * time )

    def Transform(self, matrix):
        newPointTuple = matrix.TimesTuple(self.Origin())
        assert isclose( newPointTuple[3], 1.0 )
        newVectorTuple = matrix.TimesTuple(self.Direction())
        assert isclose( newVectorTuple[3], 0.0 )
        return Ray( Point(newPointTuple[0], newPointTuple[1], newPointTuple[2]),
                    Vector(newVectorTuple[0], newVectorTuple[1], newVectorTuple[2]) )