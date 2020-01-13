#! python
#
#

from behave import given, when, then
from renderer.camera import Camera
from math import pi, isclose

@when(u'{cameravar:w} ← camera({hsizevar:w}, {vsizevar:w}, {fovvar:w})')
def step_impl(context, cameravar, hsizevar, vsizevar, fovvar):
    print(u'STEP: When {} ← camera({}, {}, {})'.format(cameravar, hsizevar, vsizevar, fovvar) )
    context.result[cameravar] = Camera( context.result[hsizevar], context.result[vsizevar], context.result[fovvar] )

@then(u'{cameravar:w}.hsize = {expected:d}')
def step_impl(context, cameravar, expected):
    print(u'STEP: Then {}.hsize = {}'.format(cameravar, expected))
    assert cameravar in context.result
    result = context.result[cameravar].HSize()
    assert expected == result, 'Expected Camera {} hsize {} to be equal to {}'.format(cameravar, result, expected)


@then(u'{cameravar:w}.vsize = {expected:d}')
def step_impl(context, cameravar, expected):
    print(u'STEP: Then {}.vsize = {}'.format(cameravar, expected))
    assert cameravar in context.result
    result = context.result[cameravar].VSize()
    assert expected == result, 'Expected Camera {} vsize {} to be equal to {}'.format(cameravar, result, expected)

@given(u'{cameravar:w} ← camera({hsize:d}, {vsize:d}, π/{pi_divider:g})')
def step_impl(context, cameravar, hsize, vsize, pi_divider):
    print(u'STEP: Given {} ← camera({}, {}, π/{})'.format(cameravar, hsize, vsize, pi_divider))
    context.result[cameravar] = Camera(hsize, vsize, pi / pi_divider)

@then(u'{cameravar:w}.pixel_size = {expected:g}')
def step_impl(context, cameravar, expected):
    print(u'STEP: Then {}.pixel_size = {}'.format(cameravar, expected))
    assert cameravar in context.result
    result = context.result[cameravar].GetPixelSize()
    assert isclose(expected, result), 'Expected Camera {} pixel size {} to be equal to {}'.format(cameravar, result, expected)
