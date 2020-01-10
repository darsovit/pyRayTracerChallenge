#! python
#
# Chapter 6 'Putting It Together'
# Beginnings of a Ray Trace

from renderer.bolts import Point, Color, IdentifyHit
from renderer.canvas import Canvas
from renderer.sphere import Sphere
from renderer.rays import Ray
from renderer.material import Material
from renderer.lights import PointLight

ray_origin = Point(0, 0, -5)
wall_z     = 10
wall_size  = 7

canvas_pixels = 100
pixel_size    = wall_size / canvas_pixels
half          = wall_size / 2

canvas = Canvas( canvas_pixels, canvas_pixels )


shape  = Sphere(Material(Color(1,0.2,1), specular=0.9))

light  = PointLight(Point(-5,5,-10), Color(1,1,1))

for y in range(canvas_pixels):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x
        position = Point(world_x, world_y, wall_z)
        r = Ray(ray_origin, (position - ray_origin).normalize())
        xs = shape.Intersect( r )
        hit = IdentifyHit( xs )
        if hit:
            point = r.Position(hit['time'])
            normal = shape.Normal(point)
            eyev   = -r.Direction()
            color = shape.material.Lighting( light, point, eyev, normal )
            canvas.SetPixel( x, y, color )

imageData = canvas.ToPpm()
with open('silouhette.ppm', 'w') as f:
    f.write(imageData)
