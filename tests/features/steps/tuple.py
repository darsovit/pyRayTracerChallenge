#! python

from behave import given, then
from renderer.bolts import Tuple, Point, Vector, Color
from math import isclose, sqrt, pi
from renderer.matrix import IdentityMatrix

EPSILON = 0.0001

#def determineValue(stringval):
#    if stringval == 'π':
#        return pi
#    else:
#        return float(stringval)

#def determineNumeric(stringval):
#    fractional = stringval.split('/')
#    assert len(fractional) < 3
#    denominator = 1
#    numerator   = 1
#    if len(fractional) == 2:
#        denominator = determineValue(fractional[1])
#    sqrtsplit = fractional[0].split('√')
#    assert len(sqrtsplit) < 3
#    if len(sqrtsplit) == 2:
#        numerator *= sqrt(determineValue(sqrtsplit[1]))
#    if len(sqrtsplit[0]) > 0:
#        if len(sqrtsplit[0]) == 1 and sqrtsplit[0][0] == '-':
#            numerator *= -1
#        else:
#            numerator *= determineValue(sqrtsplit[0])
#    return numerator / denominator

@given(u'{var:w} ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var, x, y, z, w):
    print(u'STEP: {} ← tuple({}, {}, {}, {})'.format(var, x, y, z, w))
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
    #SetupContext(context)
    context.result[var] = Point(x,y,z)
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


@then(u'magnitude({var1:w}) = {val:S}')
def step_impl(context, var1, val):
    print(u'STEP: magnitude({}) = {}'.format(var1,val))
    expected = context.helpers['determineNumeric'](val)
    result = context.result[var1].magnitude()
    assert isclose(expected, result), 'Expected {} = magnitude({}) = {}'.format(expected, var1, result)


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
    #SetupContext(context)
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

@then(u'{var:w} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, var, r, g, b):
    print(u'STEP: Then {} = color({}, {}, {})'.format(var, r, g, b))
    expected = Color(r,g,b)
    result   = context.result[var]
    assert expected.compare(result), 'Expected {} to be {}, found it to be {} instead'.format( var, expected, result )

@then(u'{var1:w} * {var2:w} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, var1, var2, r, g, b):
    print(u'STEP: {} * {} = color({}, {}, {})'.format(var1,var2,r,g,b))
    expected = Color(r,g,b)
    result = context.result[var1].multiply(context.result[var2])
    assert expected == result, 'Expected {} == {} * {} = {} * {} = {}'.format(expected, var1, var2, context.result[var1], context.result[var2], result)


@when(u'{result:w} ← reflect({vectorvar:w}, {normalvar:w})')
def step_impl(context, result, vectorvar, normalvar):
    print(u'STEP: When {} ← reflect(v, n)'.format(result, vectorvar, normalvar))
    assert vectorvar in context.result
    assert normalvar in context.result
    context.result[result] = context.result[vectorvar].reflect(context.result[normalvar])


@then(u'{var:w} = vector({x:S}, {y:S}, {z:S})')
def step_impl(context, var, x, y, z):
    print(u'STEP: Then {} = vector({}, {}, {})'.format(var, x, y, z))
    assert var in context.result
    expected = Vector( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) )
    result   = context.result[var]
    assert expected.compare(result), 'Expected {} to be {}, but found it is {}'.format(var, expected, result)


@then(u'{var1:w} = normalize({var2:w})')
def step_impl(context, var1, var2):
    print(u'STEP: Then {} = normalize({})'.format(var1, var2))
    assert var1 in context.result
    assert var2 in context.result
    expected = context.result[var1]
    result = context.result[var2].normalize()
    assert expected == result, 'Expected normalize({}) = {}, found it is {} instead'.format(var2, expected, result)

@given(u'{resultvar:w} ← vector({x:S}, {y:S}, {z:S})')
def step_impl(context, resultvar, x, y, z):
    print(u'STEP: Given {} ← vector({}, {}, {})'.format(resultvar, x, y, z))
    #SetupContext(context)
    context.result[resultvar] = Vector( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) )

@then(u'{compsvar:w}.point = point({x:S}, {y:S}, {z:S})')
def step_impl(context, compsvar, x, y, z):
    print(u'STEP: Then {}.point = point({}, {}, {})'.format(compsvar, x, y, z))
    assert compsvar in context.result
    expected = Point( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) )
    result   = context.result[compsvar]['point']
    assert expected.compare(result), 'Expected computation {} point is {}, found it as {}'.format(compsvar, expected, result)


@then(u'{compsvar}.eyev = vector({x:S}, {y:S}, {z:S})')
def step_impl(context, compsvar, x, y, z):
    print(u'STEP: Then {}.eyev = vector({}, {}, {})'.format(compsvar, x, y, z))
    assert compsvar in context.result
    expected = Vector( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) )
    result   = context.result[compsvar]['eyev']
    assert expected.compare(result), 'Expected computation {} eyev is {}, found it is {}'.format( compsvar, expected, result )


@then(u'{compsvar:w}.normalv = vector({x:S}, {y:S}, {z:S})')
def step_impl(context, compsvar, x, y, z):
    print(u'STEP: Then {}.normalv = vector({}, {}, {})'.format(compsvar, x, y, z))
    assert compsvar in context.result
    expected = Vector( context.helpers['determineNumeric'](x), context.helpers['determineNumeric'](y), context.helpers['determineNumeric'](z) )
    result = context.result[compsvar]['normalv']
    assert expected.compare(result), 'Expected computation {} normalv is {}, found it is {}'.format( compsvar, expected, result )

@given(u'{var:w} ← {val:g}')
def step_impl(context, var, val):
    print(u'STEP: Given {} ← {}'.format(var, val))
    #SetupContext(context)
    context.result[var] = val


@then(u'{cameravar}.field_of_view = {val:S}')
def step_impl(context, cameravar, val):
    print(u'STEP: Then {}.field_of_view = {}'.format(cameravar, val))
    assert cameravar in context.result
    expected = context.helpers['determineNumeric'](val)
    result   = context.result[cameravar].GetFieldOfView()
    assert isclose(expected, result), 'Expected Camera {} field of view {} to be equal to expected {}, it is not'.format(cameravar, result, expected)


@given(u'{var:w} ← π/{denom:g}')
def step_impl(context, var, denom):
    print(u'STEP: Given {} ← π/{}'.format(var, denom))
    context.result[var] = pi / denom

@given(u'{var:w} ← true')
def step_impl(context, var):
    print(u'STEP: Given {} ← true'.format(var))
    context.result[var] = True

@then(u'{var:w} = {expected:g}')
def step_impl(context, var, expected):
    print(u'STEP: Then {} = {}'.format(var, expected))
    assert var in context.result
    result = context.result[var]
    assert isclose(expected, result, abs_tol=EPSILON), 'Expected variable {} to be {}, found it is {}'.format(var, expected, result)
    