#! python
#
#

from behave import given, then
from renderer.sphere import Sphere
from renderer.matrix import IdentityMatrix
from renderer.transformations import Scaling, Translation, Rotation_z
from renderer.material import Material
from renderer.bolts import Point, Color
from math import isclose, sqrt, pi


@given(u'{spherevar:w} ← sphere()')
def step_impl(context, spherevar):
    print(u'STEP: Given s ← sphere()'.format(spherevar))
    context.result[spherevar] = Sphere()
    pass

@when(u'{intersectionsvar:w} ← intersect({spherevar:w}, {rayvar:w})')
def step_impl(context, intersectionsvar, spherevar, rayvar):
    print(u'STEP: When {} ← intersect({}, {})'.format(intersectionsvar, spherevar, rayvar))
    assert spherevar in context.result
    assert rayvar in context.result
    context.result[intersectionsvar] = context.result[spherevar].Intersect(context.result[rayvar])


@then(u'{intersectionsvar:w}.count = {expected:d}')
def step_impl(context, intersectionsvar, expected):
    print(u'STEP: Then {}.count = {}'.format(intersectionsvar, expected))
    assert intersectionsvar in context.result
    result = len(context.result[intersectionsvar])
    assert expected == result, 'Expected {} intersections in {}, found {}'.format(expected, intersectionsvar, result)

@when(u'set_transform({objectvar:w}, {transformvar:w})')
def step_impl(context, objectvar, transformvar):
    print(u'STEP: When set_transform({}, {})'.format(objectvar, transformvar))
    assert objectvar in context.result
    assert transformvar in context.result
    context.result[objectvar].SetTransform( context.result[transformvar] )


@given(u'set_transform({objectvar:w}, scaling({x:g}, {y:g}, {z:g}))')
@when(u'set_transform({objectvar:w}, scaling({x:g}, {y:g}, {z:g}))')
def step_impl(context, objectvar, x, y, z):
    print(u'STEP: When set_transform({}, scaling({}, {}, {}))'.format(objectvar, x, y, z))
    assert objectvar in context.result
    context.result[objectvar].SetTransform( Scaling(x, y, z) )

@when(u'set_transform({objectvar:w}, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, objectvar, x, y, z):
    print(u'STEP: When set_transform({}, translation({}, {}, {}))'.format(objectvar, x, y, z))
    assert objectvar in context.result
    context.result[objectvar].SetTransform( Translation( x, y, z) )

@when(u'{resultvar:w} ← normal_at({objectvar:w}, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, resultvar, objectvar, x, y, z):
    print(u'STEP: When {} ← normal_at({}, point({}, {}, {}))'.format(resultvar, objectvar, x, y, z))
    assert objectvar in context.result
    context.result[resultvar] = context.result[objectvar].Normal( Point(x, y, z) )

@when(u'{resultvar:w} ← normal_at({objectvar:w}, point({x:S}, {y:S}, {z:S}))')
def step_impl(context, resultvar, objectvar, x, y, z):
    print(u'STEP: When n ← normal_at({}, point({}, {}, {}))'.format(resultvar, objectvar, x, y, z))
    assert objectvar in context.result
    context.result[resultvar] = context.result[objectvar].Normal( Point( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) ) )

@given(u'set_transform({objectvar:w}, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, objectvar, x, y, z):
    print(u'STEP: Given set_transform({}, translation({}, {}, {}))'.format(objectvar, x, y, z))
    assert objectvar in context.result
    context.result[objectvar].SetTransform( Translation(x, y, z) )

@given(u'{resultvar:w} ← scaling({scalex:g}, {scaley:g}, {scalez:g}) * rotation_z(π/{rotatez_pi_divider:g})')
def step_impl(context, resultvar, scalex, scaley, scalez, rotatez_pi_divider):
    print(u'STEP: Given {} ← scaling({}, {}, {}) * rotation_z(π/{})'.format(resultvar, scalex, scaley, scalez, rotatez_pi_divider))
    context.result[resultvar] = IdentityMatrix * Scaling(scalex, scaley, scalez) * Rotation_z( pi / rotatez_pi_divider )


@given(u'set_transform({objectvar:w}, {transformvar:w})')
def step_impl(context, objectvar, transformvar):
    print(u'STEP: Given set_transform({}, {})'.format(objectvar, transformvar))
    assert objectvar in context.result
    context.result[objectvar].SetTransform( context.result[transformvar] )



@when(u'{result} ← {spherevar}.material')
def step_impl(context, result, spherevar):
    print(u'STEP: When {} ← {}.material'.format(result, spherevar))
    assert spherevar in context.result
    context.result[result] = context.result[spherevar].Material()

@when(u'{spherevar:w}.material ← {materialvar:w}')
def step_impl(context, spherevar, materialvar):
    print(u'STEP: When {}.material ← {}'.format(spherevar, materialvar))
    assert spherevar in context.result
    assert materialvar in context.result
    context.result[spherevar].SetMaterial(context.result[materialvar])


@then(u'{spherevar:w}.material = {materialvar:w}')
def step_impl(context, spherevar, materialvar):
    print(u'STEP: Then {}.material = {}'.format(spherevar, materialvar))
    assert spherevar in context.result
    assert materialvar in context.result
    result = context.result[spherevar].Material()
    assert context.result[materialvar] == result, 'Expected Object {} material to be equal to {}, found it is {}'.format(spherevar, context.result[materialvar], result)

