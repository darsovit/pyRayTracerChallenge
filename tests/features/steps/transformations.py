#! python
#
# transformations steps

from behave import given, then
from renderer.transformations import Translation, Scaling, Rotation_x, Rotation_y, Rotation_z, Shearing, ViewTransform
from renderer.bolts import Point,Vector
from math import sqrt, pi
from renderer.matrix import IdentityMatrix

@given(u'{var:w} ← translation({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    print(u'STEP: Given {} ← translation({}, {}, {})'.format(var, x, y, z))
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
    context.result[var] = Rotation_x( pi / pi_divider )

@then(u'{transformvar:w} * {pointvar:w} = point({x:S}, {y:S}, {z:S})')
def step_impl(context, transformvar, pointvar, x, y, z):
    print(u'STEP: Then {} * {} = point({}, {}, {})'.format(transformvar, pointvar, x, y, z))
    assert transformvar in context.result
    assert pointvar     in context.result
    expected = Point(context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z))
    result = context.result[transformvar].TimesTuple(context.result[pointvar])
    assert expected.compare(result), 'Expected transform {} against point {} would result in {}, but result was {}'.format(transformvar, pointvar, expected, result)


@given(u'{var:w} ← rotation_y(π / {pi_divider:g})')
def step_impl(context, var, pi_divider):
    print(u'STEP: Given {} ← rotation_y(π / {})'.format(var, pi_divider))
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
    #SetupContext(context)
    context.result[var] = Rotation_z( pi / pi_divider )

@given(u'{var:w} ← shearing({x_y:g}, {x_z:g}, {y_x:g}, {y_z:g}, {z_x:g}, {z_y:g})')
def step_impl(context, var, x_y, x_z, y_x, y_z, z_x, z_y):
    print(u'STEP: Given {} ← shearing({}, {}, {}, {}, {}, {})'.format(var, x_y, x_z, y_x, y_z, z_x, z_y))
    context.result[var] = Shearing(x_y, x_z, y_x, y_z, z_x, z_y)

def ApplyTransform( context, transformvar, pointvar, resultvar ):
    print(u'STEP: When {} ← {} * {}'.format( resultvar, transformvar, pointvar ))
    assert pointvar in context.result
    assert transformvar in context.result
    context.result[resultvar] = context.result[transformvar].TimesTuple(context.result[pointvar])

@when(u'{resultvar:w} ← A * {pointvar:w}')
def step_impl(context, resultvar, pointvar):
    ApplyTransform( context, 'A', pointvar, resultvar )

@when(u'{resultvar:w} ← B * {pointvar:w}')
def step_impl(context, resultvar, pointvar):
    ApplyTransform( context, 'B', pointvar, resultvar )

@when(u'{resultvar:w} ← C * {pointvar:w}')
def step_impl(context, resultvar, pointvar):
    ApplyTransform( context, 'C', pointvar, resultvar )

@then(u'{pointvar:w} = point({x:g}, {y:g}, {z:g})')
def step_impl(context, pointvar, x, y, z):
    print(u'STEP: Then {} = point({}, {}, {})'.format(pointvar, x, y, z))
    assert pointvar in context.result
    expected = Point(x, y, z)
    assert expected.compare(context.result[pointvar]), 'Expected {} to equal {}, but it is {}'.format(pointvar, expected, context.result[pointvar])

@when(u'T ← C * B * A')
def step_impl(context):
    print(u'STEP: When T ← C * B * A')
    assert 'C' in context.result
    assert 'B' in context.result
    assert 'A' in context.result
    context.result['T'] = context.result['C'] * context.result['B'] * context.result['A']

@when(u'{transformvar:w} ← view_transform({fromvar:w}, {tovar:w}, {upvar:w})')
def step_impl(context, transformvar, fromvar, tovar, upvar):
    print(u'STEP: When {} ← view_transform({}, {}, {})'.format(transformvar, fromvar, tovar, upvar))
    assert fromvar in context.result
    assert tovar   in context.result
    assert upvar   in context.result
    context.result[transformvar] = ViewTransform(context.result[fromvar], context.result[tovar], context.result[upvar])


@then(u'{transformvar:w} = scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, transformvar, x, y, z):
    print(u'STEP: Then {} = scaling({}, {}, {})'.format(transformvar, x, y, z) )
    assert transformvar in context.result
    expected = Scaling( x, y, z )
    result   = context.result[transformvar]
    assert expected == result, 'Expected transform {} to be equal to scaling({}, {}, {}) matrix {}, found it as {}'.format(transformvar, x, y, z, expected, result)


@then(u'{transformvar:w} = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, transformvar, x, y, z):
    print(u'STEP: Then {} = translation({}, {}, {})'.format(transformvar, x, y, z))
    assert transformvar in context.result
    expected = Translation(x, y, z)
    result   = context.result[transformvar]
    assert expected == result, 'Expected transform {} to be equal to translation({}, {}, {})=matrix {}, found it as {}'.format(transformvar, x, y, z, expected, result)
