#! python
#
# lights.feature steps
#

from behave import given, then
from renderer.lights import PointLight
from renderer.bolts  import Point, Color

@when(u'{lightvar:w} ← point_light({positionvar:w}, {intensityvar:w})')
def step_impl(context, lightvar, positionvar, intensityvar):
    print(u'STEP: When {} ← point_light(position, intensity)'.format(lightvar, positionvar, intensityvar))
    assert positionvar in context.result
    assert intensityvar in context.result
    context.result[lightvar] = PointLight( context.result[positionvar], context.result[intensityvar] )

@given(u'{lightvar:w} ← point_light(point({pointx:g}, {pointy:g}, {pointz:g}), color({r:g}, {g:g}, {b:g}))')
def step_impl(context, lightvar, pointx, pointy, pointz, r, g, b):
    print(u'STEP: Given {} ← point_light(point({}, {}, {}), color({}, {}, {}))'.format(lightvar, pointx, pointy, pointz, r, g, b))
    if 'result' not in context:
        context.result = {}
    context.result[lightvar] = PointLight( Point(pointx, pointy, pointz), Color(r, g, b) )

@then(u'{lightvar:w}.position = {positionvar:w}')
def step_impl(context, lightvar, positionvar):
    print(u'STEP: Then {}.position = {}'.format(lightvar, positionvar))
    assert positionvar in context.result
    assert lightvar in context.result
    expected = context.result[positionvar]
    result   = context.result[lightvar].Position()
    assert expected == result, 'Expected light {} position to be {}, found it as {}'.format(lightvar, expected, result)


@then(u'{lightvar:w}.intensity = {intensityvar:w}')
def step_impl(context, lightvar, intensityvar):
    print(u'STEP: Then {}.intensity = {}'.format(lightvar, intensityvar))
    assert intensityvar in context.result
    expected = context.result[intensityvar]
    assert lightvar in context.result
    result = context.result[lightvar].Intensity()
    assert expected == result, 'Expected light {} intensity to be {}, found it as {}'.format(lightvar, expected, result)
