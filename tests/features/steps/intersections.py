#! python
#
#
from behave import given,then,when
from renderer.bolts import IdentifyHit

@when(u'{intersectionvar:w} ← intersection({time:g}, {objectvar:w})')
def step_impl(context, intersectionvar, time, objectvar):
    print(u'STEP: When i ← intersection(3.5, s)'.format(intersectionvar, time, objectvar))
    assert objectvar in context.result
    context.result[intersectionvar] = {'time': time, 'object': context.result[objectvar]}

@then(u'{intersectionvar:w}.t = {expectedtime:g}')
def step_impl(context, intersectionvar, expectedtime):
    print(u'STEP: Then i.t = 3.5'.format(intersectionvar, expectedtime))
    assert intersectionvar in context.result
    result = context.result[intersectionvar]['time']
    assert expectedtime == result, 'Expected intersection {} time to be {}, found it was {}'.format(intersectionvar, expectedtime, result)

@then(u'{intersectionvar:w}.object = {objectvar:w}')
def step_impl(context, intersectionvar, objectvar):
    print(u'STEP: Then {}.object = {}'.format(intersectionvar, objectvar))
    assert intersectionvar in context.result
    assert context.result[intersectionvar]['object'] == context.result[objectvar], 'Expected intersection {} object to be {}, found it was {}'.format( intersectionvar, context.result[objectvar], context.result[intersectionvar]['object'])

@given(u'{intersectionvar:w} ← intersection({time:g}, {objectvar:w})')
def step_impl(context, intersectionvar, time, objectvar):
    print(u'STEP: Given {} ← intersection({}, {})'.format(intersectionvar, time, objectvar))
    assert objectvar in context.result
    context.result[intersectionvar] = {'time': time, 'object': context.result[objectvar]}

@when(u'{var:w} ← intersections({intersection1var:w}, {intersection2var})')
def step_impl(context, var, intersection1var, intersection2var):
    print(u'STEP: When {} ← intersections({}, {})'.format(var, intersection1var, intersection2var))
    assert intersection1var in context.result
    assert intersection2var in context.result
    context.result[var] = [ context.result[intersection1var], context.result[intersection2var] ]

@then(u'{var:w}[{instance:d}].t = {timeval:g}')
def step_impl(context, var, instance, timeval):
    print(u'STEP: Then {}[{}].t = {}'.format(var, instance, timeval))
    assert var in context.result
    result = context.result[var][instance]['time']
    assert timeval == result, 'Expected time of {}[{}] to be {}, found {} instead'.format(var, instance, timeval, result)


@given(u'{var:w} ← intersections({intersection1var:w}, {intersection2var:w})')
def step_impl(context, var, intersection1var, intersection2var):
    print(u'STEP: Given {} ← intersections({}, {})'.format(var, intersection1var, intersection2var))
    assert intersection1var in context.result
    assert intersection2var in context.result
    context.result[var] = [ context.result[intersection1var], context.result[intersection2var] ]


@when(u'{resultvar:w} ← hit({intersectionsvar:w})')
def step_impl(context, resultvar, intersectionsvar):
    print(u'STEP: When {} ← hit({})'.format(resultvar, intersectionsvar))
    assert intersectionsvar in context.result
    context.result[resultvar] = IdentifyHit(context.result[intersectionsvar])


@then(u'{var1:w} = {var2:w}')
def step_impl(context, var1, var2):
    print(u'STEP: Then {} = {}'.format(var1, var2))
    assert context.result[var1] == context.result[var2], 'Expected {} to be equal to {}'.format(var1, var2)


@then(u'{var:w} is nothing')
def step_impl(context, var):
    print(u'STEP: Then {} is nothing'.format(var))
    assert var in context.result
    assert context.result[var] == None, 'Expected {} in context to be nothing'.format(var)


@given(u'{resultvar:w} ← intersections({var1:w}, {var2:w}, {var3:w}, {var4:w})')
def step_impl(context, resultvar, var1, var2, var3, var4):
    print(u'STEP: Given {} ← intersections({}, {}, {}, {})'.format(resultvar, var1, var2, var3, var4))
    assert var1 in context.result
    assert var2 in context.result
    assert var3 in context.result
    assert var4 in context.result
    context.result[resultvar] = [ context.result[var1]
                                , context.result[var2]
                                , context.result[var3]
                                , context.result[var4] ]
