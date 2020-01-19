#! python
from renderer.bolts import Color
from renderer.matrix import IdentityMatrix

from math import isclose

DefaultProperties = {'color':Color(1,1,1), 'ambient':0.1, 'diffuse':0.9, 'specular':0.9, 'shininess':200.0}

class Material:
    defaultColor = Color(1,1,1)
    def __init__(self,
                 color=DefaultProperties['color'],
                 ambient=DefaultProperties['ambient'],
                 diffuse=DefaultProperties['diffuse'],
                 specular=DefaultProperties['specular'],
                 shininess=DefaultProperties['shininess']):
        self.__color = color
        self.__ambient = ambient
        self.__diffuse = diffuse
        self.__specular = specular
        self.__shininess = shininess
        self.__pattern = None

    def DefaultProperties():
        return DefaultProperties

    def Color(self, position=None, objectTransform=IdentityMatrix):
        if self.__pattern:
            return self.__pattern.ColorAt(position, objectTransform)
        else:
            return self.__color

    def Ambient(self):
        return self.__ambient

    def Diffuse(self):
        return self.__diffuse

    def SetDiffuse(self, val):
        self.__diffuse = val

    def Specular(self):
        return self.__specular

    def SetSpecular(self, val):
        self.__specular = val

    def Shininess(self):
        return self.__shininess

    def SetAmbient(self, ambient):
        self.__ambient = ambient

    def SetPattern(self, pattern):
        self.__pattern = pattern

    def __eq__(self, rhs):
        return ( self.Color() == rhs.Color()
             and isclose(self.Ambient(), rhs.Ambient())
             and isclose(self.Diffuse(), rhs.Diffuse())
             and isclose(self.Specular(), rhs.Specular())
             and isclose(self.Shininess(), rhs.Shininess()) )

    def __str__(self):
        return ' '.join(list(map(str,['Color:', self.Color()
            , 'Ambient:', self.Ambient()
            , 'Diffuse:', self.Diffuse()
            , 'Specular:', self.Specular()
            , 'Shininess:', self.Shininess() ])))

    def Lighting(self, light, position, eyev, normalv, inShadow, objectTransform=IdentityMatrix):
        effectiveColor = self.Color(position, objectTransform).multiply( light.Intensity() )
        ambientColor = effectiveColor * self.Ambient()
        if inShadow:
            return Color( ambientColor[0], ambientColor[1], ambientColor[2] )
        # If not in shadow, need to combine the following
        black = Color(0,0,0)
        diffuseColor = black
        specularColor = black

        lightv = (light.Position() - position).normalize()
        lightDotNormal = lightv.dot(normalv)

        if lightDotNormal >= 0:
            diffuseColor = effectiveColor * self.Diffuse() * lightDotNormal

            reflectv = -lightv.reflect( normalv )
            reflectDotEye = reflectv.dot(eyev)
            if reflectDotEye > 0:
                factor = pow(reflectDotEye, self.Shininess())
                specularColor = light.Intensity() * self.Specular() * factor
        result = ambientColor + diffuseColor + specularColor
        return Color( result[0], result[1], result[2] )