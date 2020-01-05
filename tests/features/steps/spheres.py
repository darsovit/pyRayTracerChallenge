#! python
#
#

from behave import given, then
from renderer.sphere import Sphere
from math import isclose

@given(u'{spherevar:w} ← sphere()')
def step_impl(context, spherevar):
    print(u'STEP: Given s ← sphere()'.format(spherevar))
    if 'result' not in context:
        context.result = {}
    context.result[spherevar] = Sphere()
    pass

@when(u'{intersectionsvar:w} ← intersect({spherevar:w}, {rayvar:w})')
def step_impl(context, intersectionsvar, spherevar, rayvar):
    print(u'STEP: When {} ← intersect({}, {})'.format(intersectionsvar, spherevar, rayvar))
    assert spherevar in context.result
    assert rayvar in context.result
    context.result[intersectionsvar] = context.result[spherevar].Intersect(context.result[rayvar])


@then(u'{intersectionsvar:w}.count = {expected:d}')
def step_impl(context, intersectionsvar, expected):
    print(u'STEP: Then {}.count = {}'.format(intersectionsvar, expected))
    assert intersectionsvar in context.result
    result = len(context.result[intersectionsvar])
    assert expected == result, 'Expected {} intersections in {}, found {}'.format(expected, intersectionsvar, result)


@then(u'{var:w}[{instance:d}] = {expected:g}')
def step_impl(context, var, instance, expected):
    print(u'STEP: Then {}[{}] = {}'.format(var, instance, expected))
    assert var in context.result
    assert len(context.result[var]) > instance
    result = context.result[var][instance]
    assert isclose(expected, result), 'Expected {}[{}] == {}, found it is {}'.format(var, instance, expected, result)
    #raise NotImplementedError(u'STEP: Then xs[0] = 4.0')
