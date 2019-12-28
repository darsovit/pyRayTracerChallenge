#! python

from behave import given, then
from renderer.bolts import Tuple, Point, Vector, Color
#import renderer.bolts
from math import isclose, sqrt

#equality = renderer.bolts.equality
#isPoint  = renderer.bolts.isPoint
#isVector = renderer.bolts.isVector
#point    = renderer.bolts.point
#vector   = renderer.bolts.vector
#tupleEquality = renderer.bolts.equals
#addTuples = renderer.bolts.addTuples

EPSILON = 0.0001

#@step(r'(\a+) ← tuple\((\d+(?:\.\d+)?), (\d+(?:\.\d+)?), (\d+(?:\.\d+)?), (\d+(?:\.\d+)?)\)')
#def build_tuple(step, identifier, x, y, z, w):
	#world[identifier] = tuple(float(x), float(y), float(z), float(w))

#@step(r'(\a+)\.x = (\d+(?:\.\d+)?)')
#def test_tuple_x(step, identifier, value):
    #return ( abs(world[identifier][0] - float(value)) < EPSILON )

#@step(r'(\a+)\.y = (\d+(?:\.\d+)?)')
#def test_tuple_y(step, identifier, value):
    #return ( abs(world[identifier][1] - float(value)) < EPSILON )

#@step(r'(\a+)\.z = (\d+(?:\.\d+)?)')
#def test_tuple_z(step, identifier, value):
    #return ( abs(world[identifier][2] - float(value)) < EPSILON )

#@step(r'(\a+)\.w = (\d+(?:\.\d+)?)')
#def test_tuple_w(step, identifier, value):
    #return ( abs(world[identifier][3] - float(value)) < EPSILON )
    

@given(u'{var} ← tuple({x}, {y}, {z}, {w})')
def step_impl(context, var, x, y, z, w):
    print(u'STEP: {} ← tuple({}, {}, {}, {})'.format(var, x, y, z, w))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Tuple(float(x),float(y),float(z),float(w))
    pass

@then(u'{var}.x = {val}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.x = {}'.format(var,val))
    assert isclose(context.result[var][0],float(val)), 'Expected {}, got {}'.format(val, context.result[var][0])

@then(u'{var}.y = {val}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.y = {}'.format(var,val))
    assert isclose(context.result[var][1], float(val)), 'Expected {}, got {}'.format(val, context.result[var][1])

@then(u'{var}.z = {val}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.z = {}'.format(var,val))
    assert isclose(context.result[var][2], float(val)), 'Expected {}, got {}'.format(val, context.result[var][2])

@then(u'{var}.w = {val}')
def step_impl(context, var, val):
    print(u'STEP: THEN {}.w = {}'.format(var,val))
    assert isclose(context.result[var][3], float(val)), 'Expected {}, got {}'.format(val, context.result[var][3])


@then(u'{var} is a point')
def step_impl(context, var):
    print(u'STEP: THEN {} is a point'.format(var))
    assert context.result[var].isPoint(), 'Expected isPoint({}), got False'.format(context.result[var])


@then(u'{var} is not a vector')
def step_impl(context, var):
    print(u'STEP: THEN {} is not a vector'.format(var))
    assert not context.result[var].isVector(), 'Expected !isVector({}), got True'.format(var)


@then(u'{var} is not a point')
def step_impl(context, var):
    print(u'STEP: THEN {} is not a point'.format(var))
    assert not context.result[var].isPoint(), 'Expected !isPoint({}), got True'.format(var)


@then(u'{var} is a vector')
def step_impl(context, var):
    print(u'STEP: THEN {} is a vector'.format(var))
    assert context.result[var].isVector(), 'Expected !isVector({}), got False'.format(var)


@given(u'{var} ← point({x}, {y}, {z})')
def step_impl(context, var, x, y, z):
    print(u'STEP: {} ← point({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Point(float(x),float(y),float(z))
    pass




@given(u'{var} ← vector({x}, {y}, {z})')
def step_impl(context, var, x, y, z):
    print(u'STEP: {} ← vector({}, {}, {})'.format(var, x, y, z))
    if 'result' not in context:
        context.result = {}
    context.result[var] = Vector(float(x),float(y),float(z))
    pass

@then(u'{var1} + {var2} = tuple({x}, {y}, {z}, {w})')
def step_impl(context, var1, var2, x, y, z, w):
    print(u'STEP: {} + {} = tuple({},{},{},{})'.format(var1, var2, x, y, z, w))
    anon = (float(x),float(y),float(z),float(w))
    result = context.result[var1] + context.result[var2]
    assert anon == result, 'Expected {} == {} + {} ({} = {} + {})'.format(anon,var1, var2,result,context.result[var1],context.result[var2])


@then(u'{var1} * {scalar} = tuple({x}, {y}, {z}, {w})')
def step_impl(context, var1, scalar, x, y, z, w):
    print(u'STEP: {} * {} = tuple({}, {}, {}, {})'.format(var1, scalar, x, y, z, w))
    anon = Tuple(float(x),float(y),float(z),float(w))
    result = context.result[var1] * float(scalar)
    assert anon == result, 'Expected {} == {} * {} ({} = {} * {})'.format(anon,var1,scalar,result,context.result[var1],scalar)
    #raise NotImplementedError(u'STEP: Then a * 3.5 = tuple(3.5, -7, 10.5, -14)')


#@then(u'a * 0.5 = tuple(0.5, -1, 1.5, -2)')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then a * 0.5 = tuple(0.5, -1, 1.5, -2)')


@then(u'{var1} / {scalar} = tuple({x}, {y}, {z}, {w})')
def step_impl(context, var1, scalar, x, y, z, w):
    print(u'STEP: {} / {} = tuple({}, {}, {}, {})'.format(var1, scalar, x, y, z, w))
    anon = Tuple(float(x),float(y),float(z),float(w))
    result = context.result[var1] / float(scalar)
    assert anon == result, 'Expected {} == {} / {} ({} = {} / {})'.format(anon,var1,scalar,result,context.result[var1],scalar)
    #raise NotImplementedError(u'STEP: Then a / 2 = tuple(0.5, -1, 1.5, -2)')


@then(u'-{var1} = tuple({x}, {y}, {z}, {w})')
def step_impl(context, var1, x, y, z, w):
    print(u'STEP: -{} = tuple({}, {}, {}, {})'.format(var1, x, y, z, w))
    anon = Tuple(float(x), float(y), float(z), float(w))
    result = -context.result[var1]
    assert anon == result, 'Expected {} == -{} ({})'.format(anon,var1,result)


@then(u'{var1} = tuple({x}, {y}, {z}, {w})')
def step_impl(context, var1, x, y, z, w):
    print(u'STEP: {} = tuple({}, {}, {}, {})'.format(var1, x, y, z, w))
    anon = Tuple(float(x),float(y),float(z),float(w))
    assert anon == context.result[var1], 'Expected {} == {} ({})'.format(anon,var1, context.result['p'])

#@then(u'v = tuple({x}, {y}, {z}, {w})')
#def step_impl(context, x, y, z, w):
    #print(u'STEP: v = tuple({}, {}, {}, {})'.format(x, y, z, w))
    #anon = (float(x),float(y),float(z),float(w))
    #assert tupleEquality(anon, context.result['v']), 'Expected {} == v ({})'.format(anon,context.result['v'])




@then(u'{var1} - {var2} = vector({x}, {y}, {z})')
def step_impl(context, var1, var2, x, y, z):
    print(u'STEP: {} - {} = vector({}, {}, {})'.format(var1, var2, x, y, z))
    anon = Vector(float(x),float(y),float(z))
    result = context.result[var1] - context.result[var2]
    assert anon == result, 'Expected {} == {} - {} ({} = {} - {})'.format(anon,var1,var2,result,context.result[var1],context.result[var2])





@then(u'{var1} - {var2} = point({x}, {y}, {z})')
def step_impl(context, var1, var2, x, y, z):
    print(u'STEP: {} - {} = vector({}, {}, {})'.format(var1, var2, x, y, z))
    anon = Point(float(x),float(y),float(z))
    result = context.result[var1] - context.result[var2]
    assert anon == result, 'Expected {} == {} - {} ({} = {} - {})'.format(anon,var1,var2,result,context.result[var1],context.result[var2])
    #raise NotImplementedError(u'STEP: Then p - v = point(-2, -4, -6)')



@then(u'magnitude({var1}) = √{val}')
def step_impl(context, var1, val):
    print(u'STEP: magnitude({}) = √{}'.format(var1,val))
    assert isclose(context.result[var1].magnitude(),sqrt(float(val))), 'Expected {} = magnitude({}) = {}'.format(sqrt(float(val)),var1, context.result[var1].magnitude())
    #raise NotImplementedError(u'STEP: Then magnitude(v) = √14')

@then(u'magnitude({var1}) = {val}')
def step_impl(context, var1, val):
    print(u'STEP: magnitude({}) = {}'.format(var1,val))
    assert isclose(context.result[var1].magnitude(),float(val)), 'Expected {} = magnitude({}) = {}'.format(val, var1, context.result[var1].magnitude())






@then(u'normalize({var1}) = vector({x}, {y}, {z})')
def step_impl(context, var1, x, y, z):
    print(u'STEP: normalize({}) = vector({}, {}, {})'.format(var1, x, y, z))
    expected = Vector(float(x), float(y), float(z))
    result = context.result[var1].normalize()
    assert expected == result, 'Expected {} == normalize({}) = {}'.format( expected, var1, result )
    #raise NotImplementedError(u'STEP: Then normalize(v) = vector(1, 0, 0)')


@then(u'normalize({var1}) = approximately vector({x}, {y}, {z})')
def step_impl(context,var1,x,y,z):
    print(u'STEP: normalize({}) = approximately vector({}, {}, {})'.format(var1,x,y,z))
    expected = Vector(float(x), float(y), float(z))
    result = context.result[var1].normalize()
    assert expected.compare(result,0.00001), 'Expected {} == normalize({}) = {}'.format( expected, var1, result )


@when(u'{var1} ← normalize({var2})')
def step_impl(context, var1, var2):
    print(u'STEP: {} ← normalize({})'.format(var1,var2))
    context.result[var1] = context.result[var2].normalize()
    pass

@then(u'dot({var1}, {var2}) = {val}')
def step_impl(context,var1,var2,val):
    print(u'STEP: dot({},{}) = {}'.format(var1,var2,val))
    assert isclose(float(val),context.result[var1].dot(context.result[var2])), 'Expected {} == dot({},{}) = dot({},{})'.format( val, var1, var2, context.result[var1], context.result[var2])


@then(u'cross({var1}, {var2}) = vector({x}, {y}, {z})')
def step_impl(context,var1,var2,x,y,z):
    print(u'STEP: cross({},{}) = vector({},{},{})'.format(var1,var2,x,y,z))
    expected = Vector(float(x),float(y),float(z))
    result   = context.result[var1].cross(context.result[var2])
    assert expected == result, 'Expected {} == cross({},{}) = cross({},{}) = {}'.format(expected,var1,var2,context.result[var1],context.result[var2],result)
    #raise NotImplementedError(u'STEP: Then cross(a, b) = vector(-1, 2, -1)')


#@then(u'cross(b, a) = vector(1, -2, 1)')
#def step_impl(context):
    #raise NotImplementedError(u'STEP: Then cross(b, a) = vector(1, -2, 1)')


@given(u'{var1} ← color({red}, {green}, {blue})')
def step_impl(context, var1, red, green, blue):
    print(u'STEP: {} ← color({}, {}, {})'.format(var1,red,green,blue))
    if 'result' not in context:
        context.result = {}
    context.result[var1] = Color(float(red),float(green),float(blue))
    pass
    #raise NotImplementedError(u'STEP: Given c ← color(-0.5, 0.4, 1.7)')


@then(u'{var1}.red = {val}')
def step_impl(context, var1, val):
    print(u'STEP: {}.red = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['red'], float(val) ), 'Expected {} == {}.red = {}'.format( val, var1, context.result[var1] )
    #raise NotImplementedError(u'STEP: Then c.red = -0.5')

@then(u'{var1}.green = {val}')
def step_impl(context, var1, val):
    print(u'STEP: {}.green = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['green'], float(val) ), 'Expected {} == {}.green = {}'.format( val, var1, context.result[var1] )

@then(u'{var1}.blue = {val}')
def step_impl(context, var1, val):
    print(u'STEP: {}.blue = {}'.format(context.result[var1],val))
    assert isclose( context.result[var1]['blue'], float(val) ), 'Expected {} == {}.blue = {}'.format( val, var1, context.result[var1] )


#@given(u'c1 ← color(0.9, 0.6, 0.75)')
#def step_impl(context):
    #raise NotImplementedError(u'STEP: Given c1 ← color(0.9, 0.6, 0.75)')


#@given(u'c2 ← color(0.7, 0.1, 0.25)')
#def step_impl(context):
    #raise NotImplementedError(u'STEP: Given c2 ← color(0.7, 0.1, 0.25)')


@then(u'{var1} + {var2} = color({r}, {g}, {b})')
def step_impl(context,var1,var2,r,g,b):
    print(u'STEP: {} + {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(float(r),float(g),float(b))
    result = context.result[var1] + context.result[var2]
    assert expected == result, 'Expected {} == {} + {} = {}'.format(expected, var1, var2, result)


@then(u'{var1} - {var2} = color({r}, {g}, {b})')
def step_impl(context,var1,var2,r,g,b):
    print(u'STEP: {} - {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(float(r),float(g),float(b))
    result = context.result[var1] - context.result[var2]
    assert expected == result, 'Expected {} == {} + {} = {}'.format(expected, var1, var2, result)


@then(u'{var} * 2 = color({r}, {g}, {b})')
def step_impl(context, var,  r, g, b):
    scalar = 2
    print(u'STEP: {} * {} = color({}, {}, {})'.format(var,scalar,r,g,b))
    expected = Color(float(r),float(g),float(b))
    result = context.result[var] * scalar
    assert expected == result, 'Expected {} == {} * {} = {}'.format(expected,var,scalar,result)
    #raise NotImplementedError(u'STEP: Then c * 2 = color(0.4, 0.6, 0.8)')


#@given(u'c1 ← color(1, 0.2, 0.4)')
#def step_impl(context):
    #raise NotImplementedError(u'STEP: Given c1 ← color(1, 0.2, 0.4)')


#@given(u'c2 ← color(0.9, 1, 0.1)')
#def step_impl(context):
    #raise NotImplementedError(u'STEP: Given c2 ← color(0.9, 1, 0.1)')


@then(u'{var1} * {var2} = color({r}, {g}, {b})')
def step_impl(context, var1, var2, r, g, b):
    print(u'STEP: {} * {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(float(r),float(g),float(b))
    result = context.result[var1].multiply(context.result[var2])
    assert expected == result, 'Expected {} == {} * {} = {} * {} = {}'.format(expected, var1, var2, context.result[var1], context.result[var2], result)
    #raise NotImplementedError(u'STEP: Then c1 * c2 = color(0.9, 0.2, 0.04)')



@when(u'r ← reflect(v, n)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When r ← reflect(v, n)')



@then(u'r = vector(1, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = vector(1, 1, 0)')


@then(u'r = vector(1, 0, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = vector(1, 0, 0)')
