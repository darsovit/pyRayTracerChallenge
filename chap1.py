#! python
#
# Ray Tracer Challenge in Python
# Chap1 exercise

import renderer.bolts


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
    projectile = Projectile(renderer.bolts.Point(0,1,0), renderer.bolts.Vector(1,1,0).normalize())
    environment = Environment(renderer.bolts.Vector(0,-0.1,0), renderer.bolts.Vector(-0.01,0,0))
    
    while projectile.position[1] > 0.0:
        print(projectile.position)
        projectile.tick(environment)

