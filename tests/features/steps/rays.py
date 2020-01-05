#! python
#
# rays.feature steps
#

from behave import given, then
from renderer.rays import Ray
from renderer.bolts import Point, Vector

@when(u'{rayvar:w} ← ray({originvar:w}, {directionvar:w})')
def step_impl(context, rayvar, originvar, directionvar):
    print(u'STEP: When {} ← ray({}, {})'.format(rayvar, originvar, directionvar))
    assert originvar in context.result
    assert directionvar in context.result
    context.result[rayvar] = Ray( context.result[originvar], context.result[directionvar] )

@then(u'{rayvar:w}.origin = {originvar:w}')
def step_impl(context, rayvar, originvar):
    print(u'STEP: Then {}.origin = {}'.format(rayvar, originvar))
    assert rayvar in context.result
    assert originvar in context.result
    assert context.result[rayvar].Origin() == context.result[originvar]

@then(u'{rayvar:w}.direction = {directionvar:w}')
def step_impl(context, rayvar, directionvar):
    print(u'STEP: Then r.direction = direction'.format(rayvar, directionvar))
    assert rayvar in context.result
    assert directionvar in context.result
    assert context.result[rayvar].Direction() == context.result[directionvar]

@given(u'{rayvar:w} ← ray(point({pointx:g}, {pointy:g}, {pointz:g}), vector({vecx:g}, {vecy:g}, {vecz:g}))')
def step_impl(context, rayvar, pointx, pointy, pointz, vecx, vecy, vecz):
    print(u'STEP: Given r ← ray(point(2, 3, 4), vector(1, 0, 0))'.format(rayvar, pointx, pointy, pointz, vecx, vecy, vecz))
    if 'result' not in context:
        context.result = {}
    context.result[rayvar] = Ray(Point(pointx, pointy, pointz), Vector(vecx, vecy, vecz))

@then(u'position({rayvar:w}, {time:g}) = point({pointx:g}, {pointy:g}, {pointz:g})')
def step_impl(context, rayvar, time, pointx, pointy, pointz):
    print(u'STEP: Then position({}, {}) = point({}, {}, {})'.format(rayvar, time, pointx, pointy, pointz))
    assert rayvar in context.result
    expected = Point(pointx, pointy, pointz)
    result = context.result[rayvar].Position(time)
    assert expected == result, 'Expected ray {} position at time {} to be {}, result was {}'.format(rayvar, time, expected, result)
