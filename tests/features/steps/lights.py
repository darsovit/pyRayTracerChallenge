#! python
#
# lights.feature steps
#

from behave import given, then
from renderer.lights import PointLight

@when(u'{lightvar:w} ← point_light({positionvar:w}, {intensityvar:w})')
def step_impl(context, lightvar, positionvar, intensityvar):
    print(u'STEP: When {} ← point_light(position, intensity)'.format(lightvar, positionvar, intensityvar))
    assert positionvar in context.result
    assert intensityvar in context.result
    context.result[lightvar] = PointLight( context.result[positionvar], context.result[intensityvar] )


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