#! python
#
# Steps for matrix tests
#
from behave import given, then
from renderer.matrix import Matrix
from math import isclose

@given(u'the following {x}x{y} matrix {matrixvar}')
def step_impl(context, x, y, matrixvar):
    print(u'STEP: Given the following 4x4 matrix M'.format(x,y,matrixvar))
    if 'result' not in context:
        context.result = {}
    vals = [list(map(float,context.table.headings))]
    for row in context.table:
        vals += [list(map(float,row))]
    print(vals)
    context.result[matrixvar] = Matrix(int(x),int(y),vals)
    #raise NotImplementedError(u'STEP: Given the following 4x4 matrix M')
    pass


@then(u'{matrixvar}[{x},{y}] = {expected}')
def step_impl(context,matrixvar,x,y,expected):
    print(u'STEP: Then {}[{},{}] = {}'.format(matrixvar,x,y,expected))
    assert matrixvar in context.result, 'Expected Matrix {} in result'.format(matrixvar)
    result = context.result[matrixvar][int(x),int(y)]
    assert isclose(result, float(expected)), 'Expected val {} not equal to M[{},{}]=={}'.format(float(expected),int(x),int(y),result)
    #raise NotImplementedError(u'STEP: Then M[0,0] = 1')




#@given(u'the following 2x2 matrix M')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 2x2 matrix M')



#@given(u'the following 3x3 matrix M')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 3x3 matrix M')


@given(u'the following matrix A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following matrix A')


@given(u'the following matrix B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following matrix B')


@then(u'A = B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A = B')


@then(u'A != B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A != B')


@then(u'A * B is the following 4x4 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A * B is the following 4x4 matrix')


@then(u'A * identity_matrix = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A * identity_matrix = A')


@then(u'identity_matrix * a = a')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then identity_matrix * a = a')


@then(u'transpose(A) is the following matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then transpose(A) is the following matrix')


@given(u'A ← transpose(identity_matrix)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A ← transpose(identity_matrix)')


@then(u'A = identity_matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A = identity_matrix')


#@given(u'the following 2x2 matrix A')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 2x2 matrix A')


@then(u'determinant(A) = 17')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 17')


#@given(u'the following 3x3 matrix A')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 3x3 matrix A')


@then(u'submatrix(A, 0, 2) is the following 2x2 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 0, 2) is the following 2x2 matrix')


#@given(u'the following 4x4 matrix A')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 4x4 matrix A')


@then(u'submatrix(A, 2, 1) is the following 3x3 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 2, 1) is the following 3x3 matrix')


@given(u'B ← submatrix(A, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← submatrix(A, 1, 0)')


@then(u'determinant(B) = 25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(B) = 25')


@then(u'minor(A, 1, 0) = 25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then minor(A, 1, 0) = 25')


@then(u'minor(A, 0, 0) = -12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then minor(A, 0, 0) = -12')


@then(u'cofactor(A, 0, 0) = -12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = -12')


@then(u'cofactor(A, 1, 0) = -25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 1, 0) = -25')


@then(u'cofactor(A, 0, 0) = 56')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = 56')


@then(u'cofactor(A, 0, 1) = 12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 1) = 12')


@then(u'cofactor(A, 0, 2) = -46')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 2) = -46')


@then(u'determinant(A) = -196')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -196')


@then(u'cofactor(A, 0, 0) = 690')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = 690')


@then(u'cofactor(A, 0, 1) = 447')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 1) = 447')


@then(u'cofactor(A, 0, 2) = 210')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 2) = 210')


@then(u'cofactor(A, 0, 3) = 51')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 3) = 51')


@then(u'determinant(A) = -4071')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -4071')


@then(u'determinant(A) = -2120')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -2120')


@then(u'A is invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is invertible')


@then(u'determinant(A) = 0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 0')


@then(u'A is not invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is not invertible')


@given(u'B ← inverse(A)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← inverse(A)')


@then(u'determinant(A) = 532')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 532')


@then(u'cofactor(A, 2, 3) = -160')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 2, 3) = -160')


#@then(u'B[3,2] = -160/532')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then B[3,2] = -160/532')


@then(u'cofactor(A, 3, 2) = 105')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 3, 2) = 105')


#@then(u'B[2,3] = 105/532')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then B[2,3] = 105/532')


@then(u'B is the following 4x4 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then B is the following 4x4 matrix')


@then(u'inverse(A) is the following 4x4 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then inverse(A) is the following 4x4 matrix')


#@given(u'the following 4x4 matrix B')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given the following 4x4 matrix B')


@given(u'C ← A * B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given C ← A * B')


@then(u'C * inverse(B) = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then C * inverse(B) = A')