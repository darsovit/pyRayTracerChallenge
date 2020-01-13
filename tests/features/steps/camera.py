#! python
#
#

from behave import given, when, then
from renderer.camera import Camera
from math import pi, isclose
from renderer.transformations import Rotation_y, Translation, ViewTransform

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

@when(u'{rayvar:w} ← ray_for_pixel({cameravar:w}, {x:d}, {y:d})')
def step_impl(context, rayvar, cameravar, x, y):
    print(u'STEP: When {} ← ray_for_pixel({}, {}, {})'.format(rayvar, cameravar, x, y))
    assert cameravar in context.result
    context.result[rayvar] = context.result[cameravar].RayForPixel(x, y)

@when(u'{cameravar:w}.transform ← rotation_y(π/{rotation_pi_divider:g}) * translation({transx:g}, {transy:g}, {transz:g})')
def step_impl(context, cameravar, rotation_pi_divider, transx, transy, transz):
    print(u'STEP: When {}.transform ← rotation_y(π/{}) * translation({}, {}, {})'.format(cameravar, rotation_pi_divider, transx, transy, transz))
    assert cameravar in context.result
    context.result[cameravar].SetTransform( Rotation_y( pi / rotation_pi_divider) * Translation( transx, transy, transz ) )

@given(u'{cameravar:w}.transform ← view_transform({fromvar:w}, {tovar:w}, {upvar:w})')
def step_impl(context, cameravar, fromvar, tovar, upvar):
    print(u'STEP: Given {}.transform ← view_transform({}, {}, {})'.format(cameravar, fromvar, tovar, upvar))
    assert cameravar in context.result
    assert fromvar in context.result
    assert tovar in context.result
    assert upvar in context.result
    context.result[cameravar].SetTransform( ViewTransform( context.result[fromvar], context.result[tovar], context.result[upvar] ) )

@when(u'{imagevar:w} ← render({cameravar:w}, {worldvar:w})')
def step_impl(context, imagevar, cameravar, worldvar):
    print(u'STEP: When {} ← render({}, {})'.format(imagevar, cameravar, worldvar))
    assert cameravar in context.result
    assert worldvar in context.result
    context.result[imagevar] = context.result[cameravar].Render( context.result[worldvar] )
