#! python
#
#

from renderer.bolts import Color

class Canvas:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixels = {}

    def Pixel(self, x, y):
        if (x,y) in self.pixels:
            return self.pixels[(x,y)]
        else:
            return Color(0,0,0)

    def SetPixel(self, x, y, color):
        if x < self.width and y < self.height:
            self.pixels[(x,y)] = color

    def Width(self):
        return self.width

    def Height(self):
        return self.height

    def ToPpm(self):
        lines = ['P3', ' '.join([str(self.width),str(self.height)]), '255']
        for y in range(self.height):           
            line = []
            for x in range(self.width):
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