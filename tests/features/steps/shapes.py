#! python
#
#

from behave import given, then, when
from renderer.transformations import Translation, Scaling
from renderer.shape import Shape
from renderer.sphere import Sphere
from renderer.bolts import Point, Vector, Color
from renderer.plane import Plane
from renderer.material import Material
from parse import *
from parse import compile
from renderer.matrix import IdentityMatrix
from math import isclose

class TestShape(Shape):

    def LocalIntersect(self, localRay):
        self.__savedRay = localRay

    def SavedRay(self):
        return self.__savedRay

    def LocalNormal(self, localPoint):
        return Vector( localPoint[0], localPoint[1], localPoint[2] )



@then(u'{objectvar:w}.transform = {expectedvar:w}')
def step_impl(context, objectvar, expectedvar):
    print(u'STEP: Then {}.transform = {}'.format(objectvar, expectedvar))
    assert objectvar   in context.result
    assert expectedvar in context.result
    expected = context.result[expectedvar]
    result   = context.result[objectvar].Transform()
    assert expected == result, 'Expected object {} transform matrix to be {}, found {}'.format(objectvar, expected, result)

@given(u'{shapevar:w} ← test_shape()')
def step_impl(context, shapevar):
    print(u'STEP: Given {} ← test_shape()'.format(shapevar))
    context.result[shapevar] = TestShape()
    assert context.result[shapevar] is not None

@then(u'{shapevar:w}.transform = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, shapevar, x, y, z):
    print(u'STEP: Then {}.transform = translation({}, {}, {})'.format(shapevar, x, y, z))
    assert shapevar in context.result
    context.result[shapevar].SetTransform( Translation(x, y, z) )

@then(u'{shapevar:w}.saved_ray.origin = point({x:g}, {y:g}, {z:g})')
def step_impl(context, shapevar, x, y, z):
    print(u'STEP: Then {}.saved_ray.origin = point({}, {}, {})'.format(shapevar, x, y, z))
    assert shapevar in context.result
    expected = Point(x, y, z)
    result   = context.result[shapevar].SavedRay().Origin()
    assert expected.compare(result), 'Expected {} saved ray origin = {}, but instead it is {}'.format(shapevar, expected, result)

@then(u'{shapevar:w}.saved_ray.direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, shapevar, x, y, z):
    print(u'STEP: Then {}.saved_ray.direction = vector({}, {}, {})'.format(shapevar, x, y, z))
    assert shapevar in context.result
    expected = Vector( x, y, z )
    result = context.result[shapevar].SavedRay().Direction()
    assert expected.compare(result), 'Expected {} saved ray direction = {}, but instead it is {}'.format(shapevar, expected, result)

@when(u'{normalvar:w} ← local_normal_at({objectvar:w}, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, normalvar, objectvar, x, y, z):
    print(u'STEP: When {} ← local_normal_at({}, point({}, {}, {}))'.format(normalvar, objectvar, x, y, z))
    assert objectvar in context.result
    context.result[normalvar] = context.result[objectvar].LocalNormal( Point(x, y, z) )

@when(u'{intersectionsvar:w} ← local_intersect({objectvar:w}, {rayvar:w})')
def step_impl(context, intersectionsvar, objectvar, rayvar):
    print(u'STEP: When {} ← local_intersect({}, {})'.format(intersectionsvar, objectvar, rayvar))
    assert objectvar in context.result
    assert rayvar in context.result
    context.result[intersectionsvar] = context.result[objectvar].LocalIntersect( context.result[rayvar] )

@given(u'{planevar:w} ← plane()')
def step_impl(context, planevar):
    print(u'STEP: Given {} ← plane()'.format(planevar))
    context.result[planevar] = Plane()


def buildMaterial( materialProps ):
    aMaterial = {}
    for prop in Material.DefaultProperties():
        if prop in materialProps and prop != 'color':
            aMaterial[prop] = float(materialProps[prop])
        elif prop in materialProps and prop == 'color':
            result = parse('({r:g}, {g:g}, {b:g})', materialProps[prop])
            aMaterial[prop] = Color( result['r'], result['g'], result['b'] )
        else:
            aMaterial[prop] = Material.DefaultProperties()[prop]
    return Material(color=aMaterial['color'], ambient=aMaterial['ambient'], diffuse=aMaterial['diffuse'], specular=aMaterial['specular'], shininess=aMaterial['shininess'], reflectivity=aMaterial['reflective'])

def buildTransforms( transforms ):
    transformParse = compile('{transform:w}({x:g}, {y:g}, {z:g})')
    finalTransform = IdentityMatrix
    for transform in transforms:
        result = transformParse.parse(transform)
        if result['transform'] == 'scaling':
            finalTransform = finalTransform * Scaling( result['x'], result['y'], result['z'] )
        elif result['transform'] == 'translation':
            finalTransform = finalTransform * Translation( result['x'], result['y'], result['z'] )
        else:
            assert False, 'Unhandled transform: {}'.format(transform)
    return finalTransform

def buildShapeDetailsFromProps(props):
    materialProps = {}
    transforms    = []
    for sphereProp in props:
        embeddedProps = sphereProp.split('.')
        if len(embeddedProps) > 1 and embeddedProps[0] == 'material':
            materialProps[embeddedProps[1]] = props[sphereProp]
        if len(embeddedProps) == 1 and embeddedProps[0] == 'transform':
            transforms += [ props[sphereProp] ]
    material = buildMaterial( materialProps )
    transform = buildTransforms( transforms )
    return ( transform, material )

def buildShapeDetailsFromTable(context):
    props = {}
    (key,value) = context.table.headings
    props[key] = value
    for row in context.table:
        (key,value) = row
        props[key] = value
    return buildShapeDetailsFromProps(props)

@given(u'{spherevar} ← sphere() with')
def step_impl(context, spherevar):
    print(u'STEP: Given {} ← sphere() with'.format(spherevar))
    (transform,material) = buildShapeDetailsFromTable(context)
    context.result[spherevar] = Sphere(transform, material)

@given(u'{shapevar:w} ← plane() with')
def step_impl(context, shapevar):
    print(u'STEP: Given {} ← plane() with'.format(shapevar))
    (transform,material) = buildShapeDetailsFromTable(context)
    context.result[shapevar] = Plane(transform, material)


@given(u'{objectvar:w}.material.ambient ← {ambientval:g}')
def step_impl(context, objectvar, ambientval):
    print(u'STEP: Given {}.material.ambient ← {}'.format(objectvar, ambientval))
    assert objectvar in context.result
    context.result[objectvar].Material().SetAmbient(ambientval)

@then(u'{colorvar} = {objectvar}.material.color')
def step_impl(context, colorvar, objectvar):
    print(u'STEP: Then {} = {}.material.color'.format(colorvar, objectvar))
    assert objectvar in context.result
    expected = context.result[objectvar].Material().Color()
    result   = context.result[colorvar]
    assert expected.compare(result), 'Expected color {} to equal object {} material color {}, but it is instead {}'.format(colorvar, objectvar, expected, result)

@then(u'{objectvar}.material.reflective = {expected:g}')
def step_impl(context, objectvar, expected):
    print(u'STEP: Then {}.material.reflective = {}'.format(objectvar, expected))
    assert objectvar in context.result
    result = context.result[objectvar].Material().Reflectivity()
    assert isclose(expected, result), 'Expected {} material reflectivity to be {}, found it as {}'.format(objectvar, expected, result)