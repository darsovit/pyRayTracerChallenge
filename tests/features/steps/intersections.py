#! python
#
#
from behave import given,then,when
from renderer.bolts import IdentifyHit, EPSILON, Vector
from math import isclose

@given(u'{intersectionvar:w} ← intersection({time:S}, {objectvar:w})')
@when(u'{intersectionvar:w} ← intersection({time:S}, {objectvar:w})')
def step_impl(context, intersectionvar, time, objectvar):
    print(u'STEP: When {} ← intersection({}, {})'.format(intersectionvar, time, objectvar))
    assert objectvar in context.result
    determineNumeric = context.helpers['determineNumeric']
    context.result[intersectionvar] = {'time': determineNumeric(time), 'object': context.result[objectvar]}

@then(u'{intersectionvar:w}.t = {expectedtime:g}')
def step_impl(context, intersectionvar, expectedtime):
    print(u'STEP: Then {}.t = {}'.format(intersectionvar, expectedtime))
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

@given(u'{var:w} ← intersections({intersection1var:w})')
def step_impl(context, var, intersection1var):
    print(u'STEP: When {} ← intersections({})'.format(var, intersection1var))
    assert intersection1var in context.result
    context.result[var] = [ context.result[intersection1var] ]

@then(u'{var:w}[{instance:d}].t = {timeval:g}')
def step_impl(context, var, instance, timeval):
    print(u'STEP: Then {}[{}].t = {}'.format(var, instance, timeval))
    assert var in context.result
    result = context.result[var][instance]['time']
    assert timeval == result, 'Expected time of {}[{}] to be {}, found {} instead'.format(var, instance, timeval, result)

@when(u'{var:w} ← intersections({intersection1var:w}, {intersection2var})')
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

@then(u'{intersectsvar:w}[{instance:d}].object = {objectvar:w}')
def step_impl(context, intersectsvar, instance, objectvar):
    print(u'STEP: Then {}[{}].object = {}'.format(intersectsvar, instance, objectvar))
    assert intersectsvar in context.result
    assert objectvar in context.result
    result = context.result[intersectsvar][instance]['object']
    expected = context.result[objectvar]
    assert expected == result, 'Expected {}[{}].object to be {}, but found {} instead'.format(intersectsvar, instance, expected, result)

@when(u'{compsvar:w} ← prepare_computations({intersectionvar:w}, {rayvar:w})')
def step_impl(context, compsvar, intersectionvar, rayvar):
    print(u'STEP: When {} ← prepare_computations({}, {})'.format(compsvar, intersectionvar, rayvar))
    assert intersectionvar in context.result
    assert rayvar in context.result
    context.result[compsvar] = context.result[intersectionvar]['object'].PrepareComputations(context.result[rayvar], context.result[intersectionvar]['time'])

@when(u'{compsvar:w} ← prepare_computations({intersectionvar:w}, {rayvar:w}, {intersectionsvar:w})')
def step_impl(context, compsvar, intersectionvar, rayvar, intersectionsvar):
    print(u'STEP: When {} ← prepare_computations({}, {}, {})'.format(compsvar, intersectionvar, rayvar, intersectionsvar))
    assert intersectionvar in context.result
    assert intersectionsvar in context.result
    assert rayvar in context.result
    context.result[compsvar] = context.result[intersectionvar]['object'].PrepareComputations(context.result[rayvar], context.result[intersectionvar]['time'], context.result[intersectionsvar])


@when(u'{compsvar:w} ← prepare_computations({intersectionsvar:w}[{instance:d}], {rayvar:w}, {intersections2var:w})')
def step_impl(context, compsvar, intersectionsvar, instance, rayvar, intersections2var):
    print(u'STEP: When {} ← prepare_computations({}[{}], {}, {})'.format(compsvar, intersectionsvar, instance, rayvar, intersections2var))
    assert intersectionsvar in context.result
    assert intersectionsvar == intersections2var
    assert len(context.result[intersectionsvar]) > instance
    assert rayvar in context.result
    context.result[compsvar] = context.result[intersectionsvar][instance]['object'].PrepareComputations(context.result[rayvar], context.result[intersectionsvar][instance]['time'], context.result[intersectionsvar])



@then(u'{compsvar:w}.t = {intersectionvar:w}.t')
def step_impl(context, compsvar, intersectionvar):
    print(u'STEP: Then {}.t = {}.t'.format(compsvar, intersectionvar))
    assert compsvar in context.result
    assert intersectionvar in context.result
    expected = context.result[intersectionvar]['time']
    result   = context.result[compsvar]['time']
    assert expected == result, 'Expected time in intersection {} to match time in computations {}, but {} != {}'.format(intersectionvar, compsvar, expected, result)


@then(u'{compsvar:w}.object = {intersectionvar:w}.object')
def step_impl(context, compsvar, intersectionvar):
    print(u'STEP: Then {}.object = {}.object'.format(compsvar, intersectionvar))
    assert compsvar in context.result
    assert intersectionvar in context.result
    expected = context.result[intersectionvar]['object']
    result   = context.result[compsvar]['object']
    assert expected == result, 'Expected object in intersection {} to match object in computations {}, but they are not the same'.format(intersectionvar, compsvar)

@then(u'{compsvar:w}.inside = false')
def step_impl(context, compsvar):
    expected = False
    print(u'STEP: Then {}.inside = {}'.format(compsvar, expected))
    assert compsvar in context.result
    result = context.result[compsvar]['inside']
    assert expected == result, 'Expected computations {} to indicate inside was {}, but found it as {}'.format(compsvar, expected, result)

@then(u'{compsvar:w}.inside = true')
def step_impl(context, compsvar):
    expected = True
    print(u'STEP: Then {}.inside = {}'.format(compsvar, expected))
    assert compsvar in context.result
    result = context.result[compsvar]['inside']
    assert expected == result, 'Expected computations {} to indicate inside was {}, but found it as {}'.format(compsvar, expected, result)

@then(u'{compsvar:w}.over_point.z < -EPSILON/2')
def step_impl(context, compsvar):
    print(u'STEP: Then {}.over_point.z < -EPSILON/2'.format(compsvar))
    assert compsvar in context.result
    expected = -EPSILON / 2
    result = context.result[compsvar]['over_point'][2]
    assert result < expected, 'Expected {}.over_point.z ({}) < -EPSILON / 2 ({})'.format(compsvar, result, expected)

@then(u'{compsvar:w}.under_point.z > EPSILON/2')
def step_impl(context, compsvar):
    print(u'STEP: Then {}.under_point.z > EPSILON/2'.format(compsvar))
    assert compsvar in context.result
    expected = EPSILON / 2
    result = context.result[compsvar]['under_point'][2]
    assert result > expected, 'Expected {}.under_point.z ({}) < EPSILON / 2 ({})'.format(compsvar, result, expected)

@then(u'{compsvar:w}.point.z < {comps2var}.under_point.z')
def step_impl(context, compsvar, comps2var):
    print(u'STEP: Then {}.point.z < {}.under_point.z'.format(compsvar, comps2var))
    assert compsvar in context.result
    assert comps2var == compsvar
    lhs = context.result[compsvar]['point'][2]
    rhs = context.result[compsvar]['under_point'][2]
    assert lhs < rhs, 'Expected {}.point.z ({}) < {}.under_point.z ({})'.format(compsvar, lhs, compsvar, rhs)

@then(u'{compsvar:w}.point.z > {comps2var:w}.over_point.z')
def step_impl(context, compsvar, comps2var):
    print(u'STEP: Then {}.point.z > {}.over_point.z'.format(compsvar, comps2var))
    assert compsvar in context.result
    assert comps2var in context.result
    lhs = context.result[compsvar]['point'][2]
    rhs = context.result[comps2var]['over_point'][2]
    assert lhs > rhs, 'Expected {}.point.z ({}) > {}.over_point.z ({})'.format(compsvar, lhs, comps2var, rhs)

@then(u'{compsvar:w}.reflectv = vector({x:S}, {y:S}, {z:S})')
def step_impl(context, compsvar, x, y, z):
    print(u'STEP: Then {}.reflectv = vector({}, {}, {})'.format(compsvar, x, y, z))
    assert compsvar in context.result
    determineNumeric = context.helpers['determineNumeric']
    expected = Vector( determineNumeric(x), determineNumeric(y), determineNumeric(z) )
    result   = context.result[compsvar]['reflectv']
    assert expected.compare(result), 'Expected {}.reflectv to equal Vector({}, {}, {}) = {}, but it is {}'.format(compsvar, x, y, z, expected, result)

@then(u'{compsvar:w}.n1 = {expected:g}')
def step_impl(context, compsvar, expected):
    print(u'STEP: Then {}.n1 = {}'.format(compsvar, expected))
    assert compsvar in context.result
    result = context.result[compsvar]['n1']
    assert isclose(expected, result), 'Expected Computations {} n1 value to be {}, found it to be {}'.format(compsvar, expected, result)

@then(u'{compsvar:w}.n2 = {expected:g}')
def step_impl(context, compsvar, expected):
    print(u'STEP: Then {}.n2 = {}'.format(compsvar, expected))
    assert compsvar in context.result
    result = context.result[compsvar]['n2']
    assert isclose(expected, result), 'Expected Computations {} n2 value to be {}, found it to be {}'.format(compsvar, expected, result)

@then(u'{intersectionsvar:w} is empty')
def step_impl(context, intersectionsvar):
    print(u'STEP: Then {} is empty'.format(intersectionsvar))
    assert intersectionsvar in context.result
    result = len( context.result[intersectionsvar] )
    assert result == 0, 'Expected {} is empty, but it has {} elements'.format(intersectionsvar, result)

@given(u'{intersectionsvar:w} ← intersections({time1:g}:{obj1:w}, {time2:g}:{obj2:w}, {time3:g}:{obj3:w}, {time4:g}:{obj4:w}, {time5:g}:{obj5:w}, {time6:g}:{obj6:w})')
def step_impl(context, intersectionsvar, time1, obj1, time2, obj2, time3, obj3, time4, obj4, time5, obj5, time6, obj6):
    print(u'STEP: Given {} ← intersections({}:{}, {}:{}, {}:{}, {}:{}, {}:{}, {}:{})'.format(intersectionsvar,
          time1, obj1, time2, obj2, time3, obj3, time4, obj4, time5, obj5, time6, obj6))
    intersections = []
    intersections += [ {'object': context.result[obj1], 'time': time1 } ]
    intersections += [ {'object': context.result[obj2], 'time': time2 } ]
    intersections += [ {'object': context.result[obj3], 'time': time3 } ]
    intersections += [ {'object': context.result[obj4], 'time': time4 } ]
    intersections += [ {'object': context.result[obj5], 'time': time5 } ]
    intersections += [ {'object': context.result[obj6], 'time': time6 } ]
    context.result[intersectionsvar] = intersections

@given(u'{xsvar:w} ← intersections({time1:S}:{obj1:w}, {time2:S}:{obj2:w})')
def step_impl(context, xsvar, time1, obj1, time2, obj2 ):
    print(u'STEP: Given {} ← intersections({}:{}, {}:{})'.format(xsvar, time1, obj1, time2, obj2))
    assert obj1 in context.result
    assert obj2 in context.result
    determineNumeric = context.helpers['determineNumeric']
    intersections = []
    intersections += [ {'object': context.result[obj1], 'time': determineNumeric(time1)} ]
    intersections += [ {'object': context.result[obj2], 'time': determineNumeric(time2)} ]
    context.result[xsvar] = intersections

@given(u'{xsvar:w} ← intersections({time1:S}:{obj1:w})')
def step_impl(context, xsvar, time1, obj1):
    print(u'STEP: Given {} ← intersections({}:{})'.format(xsvar, time1, obj1))
    assert obj1 in context.result
    determineNumeric = context.helpers['determineNumeric']
    context.result[xsvar] = [ {'object': context.result[obj1], 'time': determineNumeric(time1)} ]

@given(u'{xsvar:w} ← intersections({time1:g}:{obj1:w}, {time2:g}:{obj2:w}, {time3:g}:{obj3:w}, {time4:g}:{obj4:w})')
def step_impl(context, xsvar, time1, obj1, time2, obj2, time3, obj3, time4, obj4):
    print(u'STEP: Given {} ← intersections({}:{}, {}:{}, {}:{}, {}:{})'.format(xsvar, time1, obj1, time2, obj2, time3, obj3, time4, obj4))
    assert obj1 in context.result
    assert obj2 in context.result
    assert obj3 in context.result
    assert obj4 in context.result
    intersections = []
    intersections += [ {'object': context.result[obj1], 'time': time1} ]
    intersections += [ {'object': context.result[obj2], 'time': time2} ]
    intersections += [ {'object': context.result[obj3], 'time': time3} ]
    intersections += [ {'object': context.result[obj4], 'time': time4} ]
    context.result[xsvar] = intersections

@when(u'{varname:w} ← schlick({compsvar:w})')
def step_impl(context, varname, compsvar):
    print(u'STEP: When {} ← schlick({})'.format(varname, compsvar))
    assert compsvar in context.result
    assert 'reflectance' in context.result[compsvar]
    context.result[varname] = context.result[compsvar]['reflectance']

