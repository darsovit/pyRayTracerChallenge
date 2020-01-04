#! python
#
# Chapter 4 'Putting It Together'
#

from renderer.canvas import Canvas
from renderer.bolts import Point, Color
from renderer.transformations import Rotation_z, Scaling, Translation
from math import pi


def BuildClock():
    Twelve = Point(0,1,0)
    oneHour = Rotation_z( -(pi / 6) )
    HoursOfClock = [Twelve]
    for i in range(11):
        HoursOfClock += [ oneHour.TimesTuple(HoursOfClock[-1]) ]
    return HoursOfClock


def CreateImage(objPts, size, color):
    transform = Translation(int(size/2), int(size/2), 0) * Scaling(int(size/2)-5, int(size/2)-5, 1)
    newPoints = []
    for point in objPts:
        newPoints += [ transform.TimesTuple( point ) ]

    canvas = Canvas( size, size )

    for pixel in newPoints:
        canvas.SetPixel( int(pixel[0]), size - int(pixel[1]), color )
    return canvas

def WriteImage(canvas, filename):
    ppmData = canvas.ToPpm()
    with open(filename, 'w') as f:
        f.write(ppmData)

WriteImage( CreateImage(BuildClock(), 50, Color(0,1,0)), 'clock.ppm')

