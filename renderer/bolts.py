#! python
#
from math import isclose, sqrt

EPSILON = 0.00001

def equality(float1, float2):
    return EPSILON > abs(float1 - float2)

class Tuple:
    def __init__(self, x, y, z, w):
        self.val = (x, y, z, w)

    def isPoint(self):
        return equality( self.val[3], 1.0 )

    def isVector(self):
        return equality( self.val[3], 0.0 )
        
    def __getitem__(self, item):
        return self.val[item]

    def compare(self,other,epsilon=EPSILON):
        return ( isclose(self.val[0],other[0],abs_tol=epsilon) and
                 isclose(self.val[1],other[1],abs_tol=epsilon) and
                 isclose(self.val[2],other[2],abs_tol=epsilon) and
                 isclose(self.val[3],other[3],abs_tol=epsilon) )
        
    def __eq__(self, other):
        return ( isclose(self.val[0],other[0]) and
                 isclose(self.val[1],other[1]) and
                 isclose(self.val[2],other[2]) and
                 isclose(self.val[3],other[3]) )
    
    def __sub__(self, other):
        return Tuple(self.val[0] - other[0], self.val[1] - other[1], self.val[2] - other[2], self.val[3] - other[3])
        
    def __add__(self, other):
        return Tuple(self.val[0] + other[0], self.val[1] + other[1], self.val[2] + other[2], self.val[3] + other[3])

    def __neg__(self):
        return Tuple(-self.val[0], -self.val[1], -self.val[2], -self.val[3])
        
    def __mul__(self, scalar):
        return Tuple(self.val[0]*scalar, self.val[1]*scalar, self.val[2]*scalar, self.val[3]*scalar)
        
    def __truediv__(self, scalar):
        return Tuple(self.val[0]/scalar, self.val[1]/scalar, self.val[2]/scalar, self.val[3]/scalar)
        
    def magnitude(self):
        assert( self.isVector() )
        return sqrt( self[0]*self[0] + self[1]*self[1] + self[2]*self[2] )

    def normalize(self):
        assert( self.isVector() )
        return self / self.magnitude()

    def __str__(self):
        return '{}'.format(self.val)

    def dot(self, other):
        return self[0] * other[0] + self[1]*other[1] + self[2]*other[2] + self[3]*other[3]


class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)

class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0.0)

    def cross(self, other):
        assert(self.isVector() and other.isVector())
        return Vector(self[1]*other[2] - self[2]*other[1],
                      self[2]*other[0] - self[0]*other[2],
                      self[0]*other[1] - self[1]*other[0])

class Color(Tuple):
    def __init__(self, r, g, b):
        super().__init__(r, g, b, 0)

    def __getitem__(self, val):
        if val == 'red':
            return super().__getitem__(0)
        elif val == 'green':
            return super().__getitem__(1)
        elif val == 'blue':
            return super().__getitem__(2)
        else:
            return super().__getitem__(val)

    def multiply(self, other):
        return Color(self[0]*other[0], self[1]*other[1], self[2]*other[2])

    def GetPpmVals(self, scale):
        red   = int(self[0] * scale + 0.5)
        red   = red if red < scale else scale
        red   = red if red >= 0 else 0
        green = int(self[1] * scale + 0.5)
        green = green if green < scale else scale
        green = green if green >= 0 else 0
        blue  = int(self[2] * scale + 0.5)
        blue  = blue if blue < scale else scale
        blue  = blue if blue >= 0 else 0
        return [ red, green, blue ]


#def isPoint( aTuple ):
#    return equality(aTuple[3], 1.0)
    
#def isVector( aTuple ):
#    return equality( aTuple[3], 0.0 )
    
#def point( x, y, z ):
#    return (x, y, z, 1.0)
    
#def vector(x, y, z):
#    return (x, y, z, 0.0)

#def equals( a, b ):
#    return equality(a[0],b[0]) and equality(a[1],b[1]) and equality(a[2],b[2]) and equality(a[3],b[3])
    
#def addTuples( a, b ):
#    return (a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])
    
