#! python
#
# steps for materials feature

from behave import given, then, when
from renderer.material import Material
from renderer.bolts import Color

from math import isclose

@given(u'{materialvar:w} ← material()')
def step_impl(context, materialvar):
    print(u'STEP: Given {} ← material()'.format(materialvar))
    if 'result' not in context:
        context.result = {}
    context.result[materialvar] = Material()

@then(u'{materialvar}.color = color({r:g}, {g:g}, {b:g})')
def step_impl(context, materialvar, r, g, b):
    print(u'STEP: Then {}.color = color({}, {}, {})'.format(materialvar, r, g, b))
    assert materialvar in context.result
    expected = Color(r, g, b)
    result   = context.result[materialvar].Color()
    assert expected == result, 'Expected color of material {} to be {}, found it is {}'.format(materialvar, expected, result)

@then(u'{materialvar:w}.ambient = {expected:g}')
def step_impl(context, materialvar, expected):
    print(u'STEP: Then {}.ambient = {}'.format(materialvar, expected))
    assert materialvar in context.result
    result = context.result[materialvar].Ambient()
    assert isclose(expected, result), 'Expected ambient of material {} to be {}, found it is {}'.format(materialvar, expected, result)

@then(u'{materialvar:w}.diffuse = {expected:g}')
def step_impl(context, materialvar, expected):
    print(u'STEP: Then {}.diffuse = {}'.format(materialvar, expected))
    assert materialvar in context.result
    result = context.result[materialvar].Diffuse()
    assert isclose(result, expected), 'Expected diffuse value of material {} to be {}, found it as {}'.format(materialvar, expected, result)


@then(u'{materialvar:w}.specular = {expected:g}')
def step_impl(context, materialvar, expected):
    print(u'STEP: Then {}.specular = {}'.format(materialvar, expected))
    assert materialvar in context.result
    result = context.result[materialvar].Specular()
    assert isclose(expected, result), 'Expected specular value of material {} to be {}, found it as {}'.format(materialvar, expected, result)


@then(u'{materialvar:w}.shininess = {expected:g}')
def step_impl(context, materialvar, expected):
    print(u'STEP: Then {}.shininess = {}'.format(materialvar, expected))
    assert materialvar in context.result
    result = context.result[materialvar].Shininess()
    assert isclose(expected, result), 'Expected shininess value of material {} to be {}, found it is {}'.format(materialvar, expected, result)

@then(u'{var:w} = material()')
def step_impl(context, var):
    print(u'STEP: Then {} = material()'.format(var))
    result = context.result[var]
    expected = Material()
    assert expected == result, 'Expected material {} to be the default material {}, found it as {}'.format(var, expected, result)

@given(u'{materialvar:w}.ambient ← {ambientval:g}')
def step_impl(context, materialvar, ambientval):
    print(u'STEP: Given {}.ambient ← {}'.format(materialvar, ambientval))
    assert materialvar in context.result
    context.result[materialvar].SetAmbient(ambientval)

@when(u'{resultvar:w} ← lighting({materialvar:w}, {lightvar:w}, {positionvar:w}, {eyevar:w}, {normalvar:w})')
def step_impl(context, resultvar, materialvar, lightvar, positionvar, eyevar, normalvar):
    print(u'STEP: When {} ← lighting(m, light, position, eyev, normalv)'.format(resultvar, materialvar, lightvar, positionvar, eyevar, normalvar))
    assert materialvar in context.result
    assert lightvar in context.result
    assert positionvar in context.result
    assert eyevar in context.result
    assert normalvar in context.result
    context.result[resultvar] = context.result[materialvar].Lighting( context.result[lightvar], context.result[positionvar], context.result[eyevar], context.result[normalvar] )

