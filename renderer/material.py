#! python
from renderer.bolts import Color

from math import isclose

class Material:
    def __init__(self):
        self.color = Color(1,1,1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def Color(self):
        return self.color

    def Ambient(self):
        return self.ambient

    def Diffuse(self):
        return self.diffuse

    def Specular(self):
        return self.specular

    def Shininess(self):
        return self.shininess

    def SetAmbient(self, ambient):
        self.ambient = ambient

    def __eq__(self, rhs):
        return ( self.Color() == rhs.Color()
             and isclose(self.Ambient(), rhs.Ambient())
             and isclose(self.Diffuse(), rhs.Diffuse())
             and isclose(self.Specular(), rhs.Specular())
             and isclose(self.Shininess(), rhs.Shininess()) )


    def Lighting(self, light, position, eyev, normalv):
        effectiveColor = self.color.multiply( light.Intensity() )
        ambientColor = effectiveColor * self.ambient
        black = Color(0,0,0)
        diffuseColor = black
        specularColor = black

        lightv = (light.Position() - position).normalize()
        lightDotNormal = lightv.dot(normalv)

        if lightDotNormal >= 0:
            diffuseColor = effectiveColor * self.diffuse * lightDotNormal

            reflectv = -lightv.reflect( normalv )
            reflectDotEye = reflectv.dot(eyev)
            if reflectDotEye > 0:
                factor = pow(reflectDotEye, self.shininess)
                specularColor = Color(1,1,1).multiply( light.Intensity() ) * self.specular * factor
        return ambientColor + diffuseColor + specularColor