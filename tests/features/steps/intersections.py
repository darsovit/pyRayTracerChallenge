#! python
#
#

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
    #raise NotImplementedError(u'STEP: Then xs[0].t = 1')