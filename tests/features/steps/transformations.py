#! python
#
# transformations steps

from behave import given, then
from renderer.transformations import Translation, Scaling, Rotation_x, Rotation_y, Rotation_z
from renderer.bolts import Point,Vector
from math import sqrt, pi

@given(u'{var:w} ← translation({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    print(u'STEP: Given {} ← translation({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Translation( x, y, z )


@then(u'{transformvar:w} * {var:w} = point({x:g}, {y:g}, {z:g})')
def step_impl(context, transformvar, var, x, y, z):
    print(u'STEP: Then {} * {} = point({}, {}, {})'.format(transformvar, var, x, y, z))
    assert transformvar in context.result
    assert var in context.result
    result = context.result[transformvar].TimesTuple(context.result[var])
    expected = Point(x, y, z)
    assert expected.compare(result), 'Expected transform {} of {} would result in point {}, instead: {}'.format(transformvar, var, expected, result)

@then(u'transform * v = v')
def step_impl(context):
    print(u'STEP: Then transform * v = v')
    transformvar = 'transform'
    vectorvar    = 'v'
    assert transformvar in context.result
    assert vectorvar    in context.result
    result = context.result[transformvar].TimesTuple(context.result[vectorvar])
    assert result == context.result[vectorvar], 'Expected transform against vector {} would result in same vector'.format(vectorvar)

@given(u'{var:w} ← scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    print(u'STEP: Given {} ← scaling({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Scaling( x, y, z )

@then(u'{var:w} * {vectorvar:w} = vector({x:g}, {y:g}, {z:g})')
def step_impl(context,var,vectorvar,x,y,z):
    print(u'STEP: Then {} * {} = vector({}, {}, {})'.format(var,vectorvar,x,y,z))
    assert var in context.result
    assert vectorvar in context.result
    expected = Vector(x,y,z)
    result   = context.result[var].TimesTuple(context.result[vectorvar])
    assert expected == result, 'Expected transform {} against vector {} would result in {}, but result was {}'.format(var, vectorvar, expected, result)

@given(u'{var:w} ← rotation_x(π / {pi_divider:g})')
def step_impl(context, var, pi_divider):
    print(u'STEP: Given {} ← rotation_x(π / {})'.format(var, pi_divider))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Rotation_x( pi / pi_divider )

@then(u'{transformvar:w} * {pointvar:w} = point(0, √2/2, √2/2)')
def step_impl(context, transformvar, pointvar):
    print(u'STEP: Then {} * {} = point(0, √2/2, √2/2)'.format(transformvar, pointvar))
    assert transformvar in context.result
    assert pointvar     in context.result
    expected = Point(0, sqrt(2)/2, sqrt(2)/2)
    result = context.result[transformvar].TimesTuple(context.result[pointvar])
    assert expected.compare(result), 'Expected transform {} against point {} would result in {}, but result was {}'.format(transformvar, pointvar, expected, result)

@then(u'{transformvar:w} * {pointvar:w} = point(0, √2/2, -√2/2)')
def step_impl(context, transformvar, pointvar):
    print(u'STEP: Then {} * {} = point(0, √2/2, -√2/2)'.format(transformvar, pointvar))
    assert transformvar in context.result
    assert pointvar     in context.result
    expected = Point(0, sqrt(2)/2, -(sqrt(2)/2))
    result = context.result[transformvar].TimesTuple(context.result[pointvar])
    assert expected.compare(result), 'Expected transform {} against point {} would result in {}, but result was {}'.format(transformvar, pointvar, expected, result)

@given(u'{var:w} ← rotation_y(π / {pi_divider:g})')
def step_impl(context, var, pi_divider):
    print(u'STEP: Given {} ← rotation_y(π / {})'.format(var, pi_divider))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Rotation_y( pi / pi_divider )

@then(u'{transformvar:w} * {pointvar:w} = point(√2/2, 0, √2/2)')
def step_impl(context, transformvar, pointvar):
    print(u'STEP: Then {} * {} = point(√2/2, 0, √2/2)'.format(transformvar, pointvar))
    assert transformvar in context.result
    assert pointvar in context.result
    expected = Point( sqrt(2)/2, 0, sqrt(2)/2 )
    result = context.result[transformvar].TimesTuple(context.result[pointvar])
    assert expected.compare(result), 'Expected transform {} against point {} would result in {}, but result was {}'.format(transformvar, pointvar, expected, result)

@given(u'{var:w} ← rotation_z(π / {pi_divider:g})')
def step_impl(context, var, pi_divider):
    print(u'STEP: Given {} ← rotation_z(π / {})'.format(var, pi_divider))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Rotation_z( pi / pi_divider )

@then(u'{transformvar:w} * {pointvar:w} = point(-√2/2, √2/2, 0)')
def step_impl(context, transformvar, pointvar):
    print(u'STEP: Then {} * {} = point(-√2/2, √2/2, 0)'.format(transformvar, pointvar))
    assert transformvar in context.result
    assert pointvar     in context.result
    expected = Point( -sqrt(2)/2, sqrt(2)/2, 0 )
    result = context.result[transformvar].TimesTuple( context.result[pointvar] )
    assert expected.compare(result), 'Expected transform {} against point {} would result in {}, but result was {}'.format(transformvar, pointvar, expected, result)
