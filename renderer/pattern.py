#! python
#
#
from renderer.matrix import IdentityMatrix
from renderer.bolts import Color
from math import floor, sqrt

class Pattern:
    def __init__(self):
        self.SetTransform(IdentityMatrix)

    def SetTransform(self, transform):
        self.__transform = transform
        self.__transformInverse = self.Transform().Inverse()

    def Transform(self):
        return self.__transform
    def TransformInverse(self):
        return self.__transformInverse

    def ColorAt(self, point, objecttransform=IdentityMatrix):
        objectPoint = objecttransform.TimesTuple(point)
        patternPoint = self.TransformInverse().TimesTuple(objectPoint)
        return self.LocalColorAt( patternPoint )

class RepeatingPattern(Pattern):
    def __init__(self, colors):
        super().__init__()
        self.__colors = colors

    def GetColors(self):
        return self.__colors

    def LocalColorAt(self, point):
        return self.GetColors()[ self.GetPos( point, len(self.GetColors()) ) ]

class StripePattern(RepeatingPattern):
    def GetPos(self, point, length):
        return floor(point[0]) % length

class GradientPattern(Pattern):
    def __init__(self, colors):
        super().__init__()
        self.__colors = colors

    def GetColors(self):
        return self.__colors

    def LocalColorAt(self, point):
        colors = self.GetColors()
        firstColorIndex = floor(point[0]) % len(colors)
        secondColorIndex = ( firstColorIndex + 1 ) % len(colors)
        distance = colors[secondColorIndex] - colors[firstColorIndex]
        fraction = point[0] - floor(point[0])
        gradientColor = colors[firstColorIndex] + distance * fraction
        return Color( gradientColor[0], gradientColor[1], gradientColor[2] )

class RingPattern(RepeatingPattern):
    def GetPos(self, point, length):
        return floor( sqrt( point[0] * point[0] + point[2] * point[2] ) ) % length

class CheckerPattern(RepeatingPattern):
    def GetPos(self, point, length):
        return (floor(point[0]) + floor(point[1]) + floor(point[2])) % length