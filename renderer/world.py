#! python
#

class World:
    def __init__(self, objects=[], lights=[]):
        self.__objects = objects
        self.__lights  = lights

    def NumObjects(self):
        return len(self.__objects)

    def NumLights(self):
        return len(self.__lights)

    def Lights(self):
        return self.__lights

    def Objects(self):
        return self.__objects