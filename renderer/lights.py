#! python
#
#

class PointLight:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def Position(self):
        return self.position

    def Intensity(self):
        return self.intensity

    def __eq__(self, rhs):
        return self.Position() == rhs.Position() and self.Intensity() == rhs.Intensity()