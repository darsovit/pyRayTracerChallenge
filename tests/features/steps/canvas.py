#! python
#
# Steps for canvas tests

from behave import given, then
from renderer.canvas import Canvas
from renderer.bolts import Color

@given(u'{var} ← canvas({width}, {height})')
def step_impl(context, var, width, height):
    print(u'STEP: Given {} ← canvas({}, {})'.format(var, width, height))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Canvas( int(width), int(height) )
    pass


@then(u'{var}.width = {width}')
def step_impl(context, var, width):
    print(u'STEP: Then {}.width = {}'.format(var,width))
    assert var in context.result, 'Expected to find canvas {} in context'.format(var)
    assert int(width) == context.result[var].Width(), 'Expected width of canvas {} in context to be {}, it is {} instead'.format(var,width, context.result[var].Width())
    #raise NotImplementedError(u'STEP: Then c.width = 10')


@then(u'{var}.height = {height}')
def step_impl(context, var, height):
    print(u'STEP: Then {}.height = {}'.format(var, height))
    assert var in context.result, 'Expected to find canvas {} in context'.format(var)
    assert int(height) == context.result[var].Height(), 'Expected height of canvas {} in context to be {}, it is {} instead'.format(var,height, context.result[var].Height())


@then(u'every pixel of {var} is color({r}, {g}, {b})')
def step_impl(context, var, r, g, b):
    print(u'STEP: Then every pixel of {} is color({}, {}, {})'.format(var, r, g, b))
    assert var in context.result, 'Expected to find canvas {} in context'.format(var)
    expected = Color( float(r), float(g), float(b) )
    for x in range(context.result[var].Width()):
        for y in range(context.result[var].Height()):
            assert expected == context.result[var].Pixel(x,y), 'Expected color ({}) at ({},{}), got color ({}) instead'.format(expected,x,y,context.result[var].Pixel(x,y))


@when(u'write_pixel({var}, {x}, {y}, {varcolor})')
def step_impl(context, var, x, y, varcolor):
    print(u'STEP: When write_pixel({}, {}, {}, {})'.format(var, x, y, varcolor))
    assert var in context.result, 'Expected to find canvas {} in context'.format(var)
    assert varcolor in context.result, 'Expected to find color {} in context'.format(varcolor)
    context.result[var].SetPixel(int(x),int(y),context.result[varcolor])
    pass


@then(u'pixel_at({var}, {x}, {y}) = {varcolor}')
def step_impl(context,var,x,y,varcolor):
    print(u'STEP: Then pixel_at({}, {}, {}) = {}'.format(var, x, y, varcolor))
    assert var in context.result, 'Expected to find canvas {} in context'.format(var)
    assert varcolor in context.result, 'Expected to find color {} in context'.format(varcolor)
    assert context.result[var].Pixel(int(x),int(y)) == context.result[varcolor], 'Expected to find color {} ({}) at Canvas {} ({}, {}) but got {}'.format( varcolor, context.result[varcolor], var, x, y, context.result[var].Pixel(x,y) )


@when(u'{ppmvar} ← canvas_to_ppm({canvasvar})')
def step_impl(context, ppmvar, canvasvar):
    print(u'STEP: When ppm ← canvas_to_ppm(c)'.format(ppmvar, canvasvar))
    assert canvasvar in context.result, 'Expected to find {} in context'.format(canvasvar)
    context.result[ppmvar] = context.result[canvasvar].ToPpm()
    pass


@then(u'lines {start}-{end} of {ppmvar} are')
def step_impl(context, start, end, ppmvar):
    print(u'STEP: Then lines {}-{} of {} are'.format(start,end,ppmvar))
    assert ppmvar in context.result, 'Expected to find {} in context as ppm data'.format(ppmvar)
    expectedlines = context.text.split('\n')
    resultlines   = context.result[ppmvar].split('\n')
    assert len(resultlines) >= int(end), 'Expected to find at least {} lines in PPM {}, but it only had {}'.format(end, ppmvar, len(resultlines))
    for i in range(int(end) - int(start) + 1):
        assert expectedlines[i] == resultlines[i+int(start)-1], 'Expected to find \'{}\' == \'{}\' as line {} in {}'.format(expectedlines[i], resultlines[i+int(start)-1], i+1, ppmvar)


@when(u'every pixel of {canvasvar} is set to color({r}, {g}, {b})')
def step_impl(context, canvasvar, r, g, b):
    print(u'STEP: When every pixel of {} is set to color({}, {}, {})'.format(canvasvar, r, g, b))
    assert canvasvar in context.result, 'Expected to find {} in context'.format(canvasvar)
    fillcolor = Color(float(r),float(g),float(b))
    for x in range(context.result[canvasvar].Width()):
        for y in range(context.result[canvasvar].Height()):
            context.result[canvasvar].SetPixel(x,y,fillcolor)
    pass


@then(u'{ppmvar} ends with a newline character')
def step_impl(context, ppmvar):
    print(u'STEP: Then {} ends with a newline character'.format(ppmvar))
    assert ppmvar in context.result, 'Expected to find {} in context'.format(ppmvar)
    assert context.result[ppmvar][-1:] == '\n', 'Expected PPM data in {} to end with a newline, have {} instead'.format(ppmvar, context.result[ppmvar][-1:])