#! python
#
# Chapter 7 'Putting It Together'
# World, Camera, and simplified rendering

from renderer.bolts import Point, Color, Vector

from renderer.sphere import Sphere

from renderer.material import Material
from renderer.lights import PointLight
from renderer.transformations import Translation, Rotation_x, Rotation_y, Scaling, ViewTransform
from renderer.world import World
from renderer.camera import Camera
from math import pi

wallMaterial = Material(color=Color(1, 0.9, 0.9), specular=0)

floor = Sphere(material=wallMaterial, transform=Scaling(10, 0.01, 10))
leftWall = Sphere(material=wallMaterial, transform = Translation(0, 0, 5) * Rotation_y(- pi/4 ) * Rotation_x( pi / 2 ) * Scaling(10, 0.01, 10) )
rightWall = Sphere(material=wallMaterial, transform = Translation(0, 0, 5) * Rotation_y( pi/4) * Rotation_x( pi/2 ) * Scaling(10, 0.01, 10) )

greenSphere = Sphere(material=Material(color=Color(0.1, 1, 0.5), diffuse=0.7, specular=0.3), transform=Translation(-0.5, 1, 0.5))
smallerSphere = Sphere(material=Material(color=Color(0.5, 1, 0.1), diffuse=0.7, specular=0.3), transform=Translation(1.5, 0.5, -0.5)*Scaling(0.5, 0.5, 0.5))
smallestSphere = Sphere(material=Material(color=Color(1, 0.8, 0.1), diffuse=0.7, specular=0.3), transform=Translation(-1.5, 0.33, -0.75) * Scaling(0.33, 0.33, 0.33))

world = World([floor, leftWall, rightWall, greenSphere, smallerSphere, smallestSphere], [PointLight(Point(-10, 10, -10), Color(1, 1, 1))])
camera = Camera(100, 50, pi / 3)
camera.SetTransform( ViewTransform(Point(0,1.5, -5), Point(0, 1, 0), Vector(0, 1, 0)) )

canvas = camera.Render(world)

imageData = canvas.ToPpm()
with open('chap7.ppm', 'w') as f:
    f.write(imageData)
