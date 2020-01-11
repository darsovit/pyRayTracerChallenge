#! python
#
#

from renderer.bolts import Color

class Canvas:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
        self.__pixels = {}

    def Pixel(self, x, y):
        if (x,y) in self.__pixels:
            return self.__pixels[(x,y)]
        else:
            return Color(0,0,0)

    def SetPixel(self, x, y, color):
        if x < self.__width and y < self.__height:
            self.__pixels[(x,y)] = color

    def Width(self):
        return self.__width

    def Height(self):
        return self.__height

    def ToPpm(self):
        lines = ['P3', ' '.join([str(self.Width()),str(self.Height())]), '255']
        for y in range(self.Height()):           
            line = []
            for x in range(self.Width()):
                line += self.Pixel(x,y).GetPpmVals(255)
            textline = str(line[0])
            for x in range(1,len(line)):
                if 70 < ( len(textline) + len(str(line[x])) + 1 ):
                    lines += [ textline ]
                    textline = str(line[x])
                else:
                    textline += ' ' + str(line[x])
            lines += [ textline ]
        return '\n'.join(lines) + '\n'