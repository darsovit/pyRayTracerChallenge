#! python

from behave import given, then
from renderer.bolts import Tuple, Point, Vector, Color
from math import isclose, sqrt

EPSILON = 0.0001

@given(u'{var:w} ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var, x, y, z, w):
    print(u'STEP: {} ← tuple({}, {}, {}, {})'.format(var, x, y, z, w))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Tuple(x,y,z,w)
    pass

@then(u'{var:w}.x = {val:g}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.x = {}'.format(var,val))
    assert isclose(context.result[var][0], val), 'Expected {}, got {}'.format(val, context.result[var][0])

@then(u'{var:w}.y = {val:g}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.y = {}'.format(var,val))
    assert isclose(context.result[var][1], val), 'Expected {}, got {}'.format(val, context.result[var][1])

@then(u'{var:w}.z = {val:g}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.z = {}'.format(var,val))
    assert isclose(context.result[var][2], val), 'Expected {}, got {}'.format(val, context.result[var][2])

@then(u'{var:w}.w = {val:g}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.w = {}'.format(var,val))
    assert isclose(context.result[var][3], val), 'Expected {}, got {}'.format(val, context.result[var][3])


@then(u'{var:w} is a point')
def step_impl(context, var):
    print(u'STEP: THEN {} is a point'.format(var))
    assert context.result[var].isPoint(), 'Expected isPoint({}), got False'.format(context.result[var])


@then(u'{var:w} is not a vector')
def step_impl(context, var):
    print(u'STEP: THEN {} is not a vector'.format(var))
    assert not context.result[var].isVector(), 'Expected !isVector({}), got True'.format(var)


@then(u'{var:w} is not a point')
def step_impl(context, var):
    print(u'STEP: THEN {} is not a point'.format(var))
    assert not context.result[var].isPoint(), 'Expected !isPoint({}), got True'.format(var)


@then(u'{var:w} is a vector')
def step_impl(context, var):
    print(u'STEP: THEN {} is a vector'.format(var))
    assert context.result[var].isVector(), 'Expected !isVector({}), got False'.format(var)


@given(u'{var:w} ← point({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    print(u'STEP: {} ← point({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Point(x,y,z)
    pass


@given(u'{var:w} ← vector({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    print(u'STEP: {} ← vector({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Vector(x,y,z)
    pass

@then(u'{var1:w} + {var2:w} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, var2, x, y, z, w):
    print(u'STEP: {} + {} = tuple({},{},{},{})'.format(var1, var2, x, y, z, w))
    expected = Tuple(x,y,z,w)
    result = context.result[var1] + context.result[var2]
    assert expected == result, 'Expected {} == {} + {} ({} = {} + {})'.format(expected,var1, var2,result,context.result[var1],context.result[var2])


@then(u'{var1:w} * {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, scalar, x, y, z, w):
    print(u'STEP: {} * {} = tuple({}, {}, {}, {})'.format(var1, scalar, x, y, z, w))
    expected = Tuple(x,y,z,w)
    result = context.result[var1] * scalar
    assert expected == result, 'Expected {} == {} * {} ({} = {} * {})'.format(expected,var1,scalar,result,context.result[var1],scalar)


@then(u'{var1:w} / {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, scalar, x, y, z, w):
    print(u'STEP: {} / {} = tuple({}, {}, {}, {})'.format(var1, scalar, x, y, z, w))
    expected = Tuple(x,y,z,w)
    result = context.result[var1] / scalar
    assert expected == result, 'Expected {} == {} / {} ({} = {} / {})'.format(expected,var1,scalar,result,context.result[var1],scalar)


@then(u'-{var1:w} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, x, y, z, w):
    print(u'STEP: -{} = tuple({}, {}, {}, {})'.format(var1, x, y, z, w))
    expected = Tuple(x,y,z,w)
    result = -context.result[var1]
    assert expected == result, 'Expected {} == -{} ({})'.format(expected,var1,result)


@then(u'{var1:w} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, x, y, z, w):
    print(u'STEP: {} = tuple({}, {}, {}, {})'.format(var1, x, y, z, w))
    assert var1 in context.result, 'Tuple {} not found in context'.format(var1)
    expected = Tuple(x,y,z,w)
    assert expected == context.result[var1], 'Expected {} == {} ({})'.format(expected,var1, context.result['p'])


@then(u'{var1:w} - {var2:w} = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, var1, var2, x, y, z):
    print(u'STEP: {} - {} = vector({}, {}, {})'.format(var1, var2, x, y, z))
    expected = Vector(x,y,z)
    assert var1 in context.result, 'Expected to find {} in context'.format(var1)
    assert var2 in context.result, 'Expected to find {} in context'.format(var2)
    result = context.result[var1] - context.result[var2]
    assert expected == result, 'Expected {} == {} - {} ({} = {} - {})'.format(expected,var1,var2,result,context.result[var1],context.result[var2])


@then(u'{var1:w} - {var2:w} = point({x:g}, {y:g}, {z:g})')
def step_impl(context, var1, var2, x, y, z):
    print(u'STEP: {} - {} = vector({}, {}, {})'.format(var1, var2, x, y, z))
    expected = Point(x,y,z)
    result = context.result[var1] - context.result[var2]
    assert expected == result, 'Expected {} == {} - {} ({} = {} - {})'.format(expected,var1,var2,result,context.result[var1],context.result[var2])


@then(u'magnitude({var1:w}) = √{val:g}')
def step_impl(context, var1, val):
    print(u'STEP: magnitude({}) = √{}'.format(var1,val))
    assert isclose(context.result[var1].magnitude(),sqrt(val)), 'Expected {} = magnitude({}) = {}'.format(sqrt(val),var1, context.result[var1].magnitude())


@then(u'magnitude({var1:w}) = {val:g}')
def step_impl(context, var1, val):
    print(u'STEP: magnitude({}) = {}'.format(var1,val))
    assert isclose(context.result[var1].magnitude(),val), 'Expected {} = magnitude({}) = {}'.format(val, var1, context.result[var1].magnitude())


@then(u'normalize({var1:w}) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, var1, x, y, z):
    print(u'STEP: normalize({}) = vector({}, {}, {})'.format(var1, x, y, z))
    expected = Vector(x,y,z)
    result = context.result[var1].normalize()
    assert expected == result, 'Expected {} == normalize({}) = {}'.format( expected, var1, result )


@then(u'normalize({var1:w}) = approximately vector({x:g}, {y:g}, {z:g})')
def step_impl(context,var1,x,y,z):
    print(u'STEP: normalize({}) = approximately vector({}, {}, {})'.format(var1,x,y,z))
    expected = Vector(x,y,z)
    result = context.result[var1].normalize()
    assert expected.compare(result,0.00001), 'Expected {} == normalize({}) = {}'.format( expected, var1, result )


@when(u'{var1:w} ← normalize({var2:w})')
def step_impl(context, var1, var2):
    print(u'STEP: {} ← normalize({})'.format(var1,var2))
    context.result[var1] = context.result[var2].normalize()
    pass

@then(u'dot({var1:w}, {var2:w}) = {val:g}')
def step_impl(context,var1,var2,val):
    print(u'STEP: dot({},{}) = {}'.format(var1,var2,val))
    assert isclose(val,context.result[var1].dot(context.result[var2])), 'Expected {} == dot({},{}) = dot({},{})'.format( val, var1, var2, context.result[var1], context.result[var2])


@then(u'cross({var1:w}, {var2:w}) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context,var1,var2,x,y,z):
    print(u'STEP: cross({},{}) = vector({},{},{})'.format(var1,var2,x,y,z))
    expected = Vector(x,y,z)
    result   = context.result[var1].cross(context.result[var2])
    assert expected == result, 'Expected {} == cross({},{}) = cross({},{}) = {}'.format(expected,var1,var2,context.result[var1],context.result[var2],result)


@given(u'{var1:w} ← color({red:g}, {green:g}, {blue:g})')
def step_impl(context, var1, red, green, blue):
    print(u'STEP: {} ← color({}, {}, {})'.format(var1,red,green,blue))
    if 'result' not in context:
        context.result = {}
    context.result[var1] = Color(red,green,blue)
    pass


@then(u'{var1:w}.red = {val:g}')
def step_impl(context, var1, val):
    print(u'STEP: {}.red = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['red'], val ), 'Expected {} == {}.red = {}'.format( val, var1, context.result[var1] )

@then(u'{var1:w}.green = {val:g}')
def step_impl(context, var1, val):
    print(u'STEP: {}.green = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['green'], val ), 'Expected {} == {}.green = {}'.format( val, var1, context.result[var1] )

@then(u'{var1:w}.blue = {val:g}')
def step_impl(context, var1, val):
    print(u'STEP: {}.blue = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['blue'], val ), 'Expected {} == {}.blue = {}'.format( val, var1, context.result[var1] )


@then(u'{var1:w} + {var2:w} = color({r:g}, {g:g}, {b:g})')
def step_impl(context,var1,var2,r,g,b):
    print(u'STEP: {} + {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(r,g,b)
    result = context.result[var1] + context.result[var2]
    assert expected == result, 'Expected {} == {} + {} = {}'.format(expected, var1, var2, result)


@then(u'{var1:w} - {var2:w} = color({r:g}, {g:g}, {b:g})')
def step_impl(context,var1,var2,r,g,b):
    print(u'STEP: {} - {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(r,g,b)
    result = context.result[var1] - context.result[var2]
    assert expected == result, 'Expected {} == {} + {} = {}'.format(expected, var1, var2, result)


@then(u'{var:w} * 2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, var, r, g, b):
    scalar = 2
    print(u'STEP: {} * {} = color({}, {}, {})'.format(var,scalar,r,g,b))
    expected = Color(r,g,b)
    result = context.result[var] * scalar
    assert expected == result, 'Expected {} == {} * {} = {}'.format(expected,var,scalar,result)


@then(u'{var1:w} * {var2:w} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, var1, var2, r, g, b):
    print(u'STEP: {} * {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(r,g,b)
    result = context.result[var1].multiply(context.result[var2])
    assert expected == result, 'Expected {} == {} * {} = {} * {} = {}'.format(expected, var1, var2, context.result[var1], context.result[var2], result)


@when(u'r ← reflect(v, n)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When r ← reflect(v, n)')


@then(u'r = vector(1, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = vector(1, 1, 0)')


@then(u'r = vector(1, 0, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = vector(1, 0, 0)')
