#! python
#
#

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def Origin(self):
        return self.origin

    def Direction(self):
        return self.direction

    def Position(self, time):
        return self.origin + ( self.direction * time )

    def Transform(self, matrix):
        return Ray( matrix.TimesTuple(self.origin), matrix.TimesTuple(self.direction) )