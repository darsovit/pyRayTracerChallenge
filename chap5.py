#! python
#
# Chapter 5 'Putting It Together'
# Beginnings of a Ray Trace

from renderer.bolts import Point, Color, IdentifyHit
from renderer.canvas import Canvas
from renderer.sphere import Sphere
from renderer.rays import Ray

ray_origin = Point(0, 0, -5)
wall_z     = 10
wall_size  = 7

canvas_pixels = 100
pixel_size    = wall_size / canvas_pixels
half          = wall_size / 2

canvas = Canvas( canvas_pixels, canvas_pixels )
color  = Color( 1, 1, 0 )
shape  = Sphere()

for y in range(canvas_pixels):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x
        position = Point(world_x, world_y, wall_z)
        r = Ray(ray_origin, (position - ray_origin).normalize())
        xs = shape.Intersect( r )
        if not IdentifyHit( xs ):
            canvas.SetPixel( x, y, color )

imageData = canvas.ToPpm()
with open('silouhette.ppm', 'w') as f:
    f.write(imageData)
