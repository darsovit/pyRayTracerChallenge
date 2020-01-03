#! python
#
# transformations steps

from behave import given, then
from renderer.transformations import Translation, Scaling
from renderer.bolts import Point,Vector

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
    assert expected == result, 'Expected transform {} of {} would result in point({}, {}, {}), instead: {}'.format(transformvar, var, x, y, z, result)


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
