#! python
#
#

from behave import given, then, when
from renderer.transformations import Translation
from renderer.shape import Shape
from renderer.bolts import Point, Vector
from renderer.plane import Plane

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
