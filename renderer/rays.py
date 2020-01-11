#! python
#
#
from renderer.bolts import Point
from math import isclose

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def Origin(self):
        return self.origin

    def Direction(self):
        return self.direction

    def Position(self, time):
        newPos = self.origin + ( self.direction * time )
        assert newPos[3] == 1
        return Point( newPos[0], newPos[1], newPos[2] )

    def Transform(self, matrix):
        return Ray( matrix.TimesTuple(self.origin), matrix.TimesTuple(self.direction) )