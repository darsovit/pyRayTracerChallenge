#! python
#
#

from behave import given, then
from renderer.sphere import Sphere

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
    #raise NotImplementedError(u'STEP: When xs ← intersect(s, r)')


@then(u'xs.count = 2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then xs.count = 2')


@then(u'xs[0] = 4.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then xs[0] = 4.0')


@then(u'xs[1] = 6.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then xs[1] = 6.0')
