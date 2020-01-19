#! python
#
#

from behave import given, then, when
from renderer.pattern import StripePattern, Pattern, GradientPattern, RingPattern, CheckerPattern
from renderer.bolts import Point, Color
from renderer.transformations import Translation, Scaling

class TestPattern(Pattern):
    def LocalColorAt(self, point):
        return Color( point[0], point[1], point[2] )

@given(u'{patternvar:w} ← stripe_pattern({color1var:w}, {color2var:w})')
def step_impl(context, patternvar, color1var, color2var):
    print(u'STEP: Given {} ← stripe_pattern({}, {})'.format(patternvar, color1var, color2var))
    context.result[patternvar] = StripePattern([context.result[color1var], context.result[color2var]])

@then(u'{patternvar:w}.a = {colorvar:w}')
def step_impl(context, patternvar, colorvar):
    print(u'STEP: Then {}.a = {}'.format(patternvar, colorvar))
    assert patternvar in context.result
    assert colorvar in context.result
    result = context.result[patternvar].GetColors()[0]
    expected = context.result[colorvar]
    assert result.compare(expected), 'Expected pattern {} color a to be equal to color {} = {}, found it as {}'.format(patternvar, colorvar, expected, result)


@then(u'{patternvar:w}.b = {colorvar:w}')
def step_impl(context, patternvar, colorvar):
    print(u'STEP: Then {}.b = {}'.format(patternvar, colorvar))
    assert patternvar in context.result
    assert colorvar in context.result
    result = context.result[patternvar].GetColors()[1]
    expected = context.result[colorvar]
    assert result.compare(expected), 'Expected pattern {} color a to be equal to color {} = {}, found it as {}'.format(patternvar, colorvar, expected, result)

@then(u'pattern_at({patternvar:w}, point({x:g}, {y:g}, {z:g})) = {colorvar:w}')
@then(u'stripe_at({patternvar:w}, point({x:g}, {y:g}, {z:g})) = {colorvar:w}')
def step_impl(context, patternvar, x, y, z, colorvar):
    print(u'STEP: Then stripe_at({}, point({}, {}, {})) = {}'.format(patternvar, x, y, z, colorvar))
    assert colorvar in context.result
    assert patternvar in context.result
    expected = context.result[colorvar]
    point = Point(x, y, z)
    result = context.result[patternvar].ColorAt( point )
    assert result.compare(expected), 'Expected pattern {} color at pos {} to be equal to color {} = {}, found it as {}'.format(patternvar, point, colorvar, expected, result)

@then(u'pattern_at({patternvar:w}, point({x:g}, {y:g}, {z:g})) = color({r:g}, {g:g}, {b:g})')
def step_impl(context, patternvar, x, y, z, r, g, b):
    print(u'STEP: Then pattern_at({}, point({}, {}, {})) = color({}, {}, {})')
    assert patternvar in context.result
    point = Point(x, y, z)
    expected = Color( r, g, b )
    result = context.result[patternvar].ColorAt( point )
    assert result.compare(expected), 'Expected pattern {} color at pos {} to be equal to color {}, found it as {}'.format(patternvar, point, expected, result)

@given(u'{materialvar:w}.pattern ← stripe_pattern(color({r1:g}, {g1:g}, {b1:g}), color({r2:g}, {g2:g}, {b2:g}))')
def step_impl(context, materialvar, r1, g1, b1, r2, g2, b2):
    print(u'STEP: Given {}.pattern ← stripe_pattern(color({}, {}, {}), color({}, {}, {}))'.format(materialvar, r1, g1, b1, r2, g2, b2))
    assert materialvar in context.result
    context.result[materialvar].SetPattern( StripePattern( [Color(r1, g1, b1), Color(r2, g2, b2)]) )

@when(u'{resultvar:w} ← pattern_at_shape({patternvar:w}, {objectvar:w}, point({x:g}, {y:g}, {z:g}))')
@when(u'{resultvar:w} ← stripe_at_object({patternvar:w}, {objectvar:w}, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, resultvar, patternvar, objectvar, x, y, z):
    print(u'STEP: When {} ← stripe_at_object({}, {}, point({}, {}, {}))'.format(resultvar, patternvar, objectvar, x, y, z))
    assert patternvar in context.result
    assert objectvar in context.result
    point = Point(x, y, z)
    context.result[resultvar] = context.result[patternvar].ColorAt(  point, context.result[objectvar].TransformInverse() )

@given(u'set_pattern_transform({patternvar:w}, scaling({x:g}, {y:g}, {z:g}))')
def step_impl(context, patternvar, x, y, z):
    print(u'STEP: Given set_pattern_transform({}, scaling({}, {}, {}))'.format(patternvar, x, y, z))
    assert patternvar in context.result
    context.result[patternvar].SetTransform( Scaling(x, y, z) )

@when(u'set_pattern_transform({patternvar:w}, translation({x:g}, {y:g}, {z:g}))')
@given(u'set_pattern_transform({patternvar:w}, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, patternvar, x, y, z):
    print(u'STEP: Given set_pattern_transform({}, translation({}, {}, {}))'.format(patternvar, x, y, z))
    assert patternvar in context.result
    context.result[patternvar].SetTransform( Translation(x, y, z) )

@given(u'{patternvar:w} ← test_pattern()')
def step_impl(context, patternvar):
    print(u'STEP: Given {} ← test_pattern()'.format(patternvar))
    context.result[patternvar] = TestPattern()

@given(u'{patternvar:w} ← gradient_pattern({color1var:w}, {color2var:w})')
def step_impl(context, patternvar, color1var, color2var):
    print(u'STEP: Given {} ← gradient_pattern({}, {})'.format(patternvar, color1var, color2var))
    assert color1var in context.result
    assert color2var in context.result
    context.result[patternvar] = GradientPattern([context.result[color1var], context.result[color2var]])

@given(u'{patternvar:w} ← ring_pattern({color1var:w}, {color2var:w})')
def step_impl(context, patternvar, color1var, color2var):
    print(u'STEP: Given {} ← ring_pattern({}, {})'.format(patternvar, color1var, color2var))
    assert color1var in context.result
    assert color2var in context.result
    context.result[patternvar] = RingPattern( [context.result[color1var], context.result[color2var] ] )

@given(u'{patternvar:w} ← checkers_pattern({color1var:w}, {color2var:w})')
def step_impl(context, patternvar, color1var, color2var):
    print(u'STEP: Given {} ← checkers_pattern({}, {})'.format(patternvar, color1var, color2var))
    assert color1var in context.result
    assert color2var in context.result
    context.result[patternvar] = CheckerPattern( [ context.result[color1var], context.result[color2var] ] )
