#! python
#
# Ray Tracer Challenge in Python
# Chap1 exercise

import renderer.bolts
import renderer.canvas

class Environment:
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind    = wind

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def tick(self, environment):
        self.position = self.position + self.velocity
        self.velocity = self.velocity + environment.gravity + environment.wind


if __name__ == '__main__':
    canvas     = renderer.canvas.Canvas(960,540)
    projectile = Projectile(renderer.bolts.Point(0,1,0), renderer.bolts.Vector(1,1.8,0).normalize() * 11.25)
    environment = Environment(renderer.bolts.Vector(0,-0.1,0), renderer.bolts.Vector(-0.01,0,0))

    positions = []
    while projectile.position[1] > 0.0:
        positions += [ projectile.position ]
        projectile.tick(environment)

    maxY = positions[0][1]
    maxX = positions[0][0]
    for position in positions:
        if position[0] > maxX:
            maxX = position[0]
        if position[1] > maxY:
            maxY = position[1]
    
    green = renderer.bolts.Color(0,1,0)
    for position in positions:
        canvas.SetPixel( int(position[0]), int(canvas.Height() - position[1]), green )
    
    ppm = canvas.ToPpm()
    with open('projectile.ppm', 'w') as f:
        f.write(ppm)
