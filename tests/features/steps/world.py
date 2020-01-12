#! python
#
#

from behave import given, when, then
from renderer.world import World
from renderer.sphere import Sphere
from renderer.material import Material
from renderer.transformations import Scaling
from renderer.lights import PointLight
from renderer.bolts import Color, Point

@given(u'{worldvar:w} ← world()')
def step_impl(context, worldvar):
    print(u'STEP: Given {} ← world()'.format(worldvar))
    if 'result' not in context:
        context.result = {}
    context.result[worldvar] = World()


@then(u'{worldvar:w} contains no objects')
def step_impl(context, worldvar):
    print(u'STEP: Then {} contains no objects'.format(worldvar))
    assert worldvar in context.result
    result = context.result[worldvar].NumObjects()
    assert result == 0, 'Expected number of objects in world {} was zero, found it was {}'.format(worldvar, result)


@then(u'{worldvar:w} has no light source')
def step_impl(context, worldvar):
    print(u'STEP: Then {} has no light source'.format(worldvar))
    assert worldvar in context.result
    result = context.result[worldvar].NumLights()
    assert 0 == result, 'Expected number of light sources in world {} was zero, found it was {}'.format(worldvar, result)

def BuildDefaultWorld():
    objects = [ Sphere(material = Material(color = Color(0.8, 1.0, 0.6), diffuse = 0.7, specular = 0.2 ))
              , Sphere(transform = Scaling(0.5, 0.5, 0.5)) ]
    lights = [ PointLight(Point(-10, 10, -10), Color(1, 1, 1)) ]
    return World( objects, lights )


@when(u'{worldvar:w} ← default_world()')
def step_impl(context, worldvar):
    print(u'STEP: When {} ← default_world()'.format(worldvar))
    if 'result' not in context:
        context.result = {}
    context.result[worldvar] = BuildDefaultWorld()

@given(u'{worldvar:w} ← default_world()')
def step_impl(context, worldvar):
    print(u'STEP: When {} ← default_world()'.format(worldvar))
    if 'result' not in context:
        context.result = {}
    context.result[worldvar] = BuildDefaultWorld()

@then(u'{worldvar:w}.light = {lightvar:w}')
def step_impl(context, worldvar, lightvar):
    print(u'STEP: Then {}.light = {}'.format(worldvar, lightvar))
    assert worldvar in context.result
    lights = context.result[worldvar].Lights()
    assert 1 == len(lights), 'Expected single light source for world'
    assert lightvar in context.result
    assert lights[0] == context.result[lightvar], 'Expected to find {} as light source in world {}, found {} not equal to {}'.format(lightvar, worldvar, lights[0], context.result[lightvar])


@then(u'{worldvar:w} contains {objectvar:w}')
def step_impl(context, worldvar, objectvar):
    print(u'STEP: Then {} contains {}'.format(worldvar, objectvar))
    assert worldvar in context.result
    assert objectvar in context.result
    foundMatchingObject = False
    for anObject in context.result[worldvar].Objects():
        if anObject == context.result[objectvar]:
            foundMatchingObject = True
        #else:
        #    print( 'No match:\n\t{}\n\t{}'.format( anObject, context.result[objectvar] ) )
    assert foundMatchingObject, 'Expected to find matching object {} in world {} among {} objects'.format(objectvar, worldvar, context.result[worldvar].NumObjects())

@when(u'{intersectionsvar:w} ← intersect_world({worldvar:w}, {rayvar:w})')
def step_impl(context, intersectionsvar, worldvar, rayvar):
    print(u'STEP: When {} ← intersect_world({}, {})'.format(intersectionsvar, worldvar, rayvar))
    assert worldvar in context.result
    assert rayvar in context.result
    context.result[intersectionsvar] = context.result[worldvar].Intersects(context.result[rayvar])

@given(u'{shapevar:w} ← the first object in {worldvar:w}')
def step_impl(context, shapevar, worldvar):
    print(u'STEP: Given {} ← the first object in {}'.format(shapevar, worldvar))
    assert worldvar in context.result
    context.result[shapevar] = context.result[worldvar].Objects()[0]

@given(u'{shapevar:w} ← the second object in {worldvar:w}')
def step_impl(context, shapevar, worldvar):
    print(u'STEP: Given {} ← the second object in {}'.format(shapevar, worldvar))
    assert worldvar in context.result
    context.result[shapevar] = context.result[worldvar].Objects()[1]
    
@when(u'{colorvar:w} ← shade_hit({worldvar:w}, {compsvar:w})')
def step_impl(context, colorvar, worldvar, compsvar):
    print(u'STEP: When {} ← shade_hit({}, {})'.format(colorvar, worldvar, compsvar))
    assert worldvar in context.result
    assert compsvar in context.result
    context.result[colorvar] = context.result[worldvar].ShadeHit( context.result[compsvar] )

@given(u'{worldvar:w}.light ← point_light(point({pointx:g}, {pointy:g}, {pointz:g}), color({r:g}, {g:g}, {b:g}))')
def step_impl(context, worldvar, pointx, pointy, pointz, r, g, b):
    print(u'STEP: Given {}.light ← point_light(point({}, {}, {}), color({}, {}, {}))'.format(worldvar, pointx, pointy, pointz, r, g, b))
    assert worldvar in context.result
    context.result[worldvar].SetLight( PointLight( Point(pointx, pointy, pointz), Color(r, g, b) ) )

@when(u'{colorvar:w} ← color_at({worldvar:w}, {rayvar:w})')
def step_impl(context, colorvar, worldvar, rayvar):
    print(u'STEP: When {} ← color_at({}, {})'.format(colorvar, worldvar, rayvar))
    assert worldvar in context.result
    assert rayvar in context.result
    context.result[colorvar] = context.result[worldvar].ColorAt( context.result[rayvar] )