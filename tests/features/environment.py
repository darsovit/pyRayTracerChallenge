#! python
#
#

import behave
from renderer.matrix import IdentityMatrix
from math import pi, sqrt

def determineValue(stringval):
    if stringval == 'π':
        return pi
    else:
        return float(stringval)

def determineNumeric(stringval):
    fractional = stringval.split('/')
    assert len(fractional) < 3
    denominator = 1
    numerator   = 1
    if len(fractional) == 2:
        denominator = determineValue(fractional[1])
    sqrtsplit = fractional[0].split('√')
    assert len(sqrtsplit) < 3
    if len(sqrtsplit) == 2:
        numerator *= sqrt(determineValue(sqrtsplit[1]))
    if len(sqrtsplit[0]) > 0:
        if len(sqrtsplit[0]) == 1 and sqrtsplit[0][0] == '-':
            numerator *= -1
        else:
            numerator *= determineValue(sqrtsplit[0])
    return numerator / denominator

def before_scenario(context, scenario):
    assert 'result' not in context
    context.result = {}
    context.result['identity_matrix'] = IdentityMatrix

def before_all(context):
    assert 'helpers' not in context
    context.helpers = {}
    context.helpers['determineNumeric'] = determineNumeric