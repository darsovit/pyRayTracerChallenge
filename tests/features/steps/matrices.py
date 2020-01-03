#! python
#
# Steps for matrix tests
#
from behave import given, then
from renderer.matrix import Matrix
from renderer.bolts  import Tuple
from math import isclose

@given(u'the following {rows:d}x{cols:d} matrix {matrixvar:w}')
def step_impl(context, rows, cols, matrixvar):
    print(u'STEP: Given the following {}x{} matrix {}'.format(rows,cols,matrixvar))
    if 'result' not in context:
        context.result = {}
    vals = [list(map(float,context.table.headings))]
    for row in context.table:
        vals += [list(map(float,row))]
    print(vals)
    context.result[matrixvar] = Matrix(rows,cols,vals)
    pass


@then(u'{matrixvar:w}[{row:d},{col:d}] = {expected:g}')
def step_impl(context,matrixvar,row,col,expected):
    print(u'STEP: Then {}[{},{}] = {}'.format(matrixvar,row,col,expected))
    assert matrixvar in context.result, 'Expected Matrix {} in result'.format(matrixvar)
    result = context.result[matrixvar][row,col]
    assert isclose(result, expected), 'Expected val {} not equal to M[{},{}]=={}'.format(expected,row,col,result)


@given(u'the following matrix {matrixvar:w}')
def step_impl(context,matrixvar):
    print(u'STEP: Given the following matrix {}'.format(matrixvar))
    if 'result' not in context:
        context.result = {}
    vals = [list(map(float,context.table.headings))]
    for row in context.table:
        vals += [list(map(float,row))]
    context.result[matrixvar] = Matrix(len(vals),len(vals[0]),vals)
    pass


# Changing these to variables makes it too generic, better to leave as specific values for matrix tests
@then(u'A = B')
def step_impl(context):
    lhs = 'A'
    rhs = 'B'
    print(u'STEP: Then {} = {}'.format(lhs,rhs))
    assert 'result' in context
    assert lhs in context.result
    assert rhs in context.result
    assert context.result[lhs] == context.result[rhs], 'Expected {} = {}'.format(lhs,rhs)


# Changing these to variables makes it too generic, better to leave as specific values for matrix tests
@then(u'A != B')
def step_impl(context):
    lhs = 'A'
    rhs = 'B'
    print(u'STEP: Then A != B')
    assert 'result' in context
    assert lhs in context.result
    assert rhs in context.result
    assert context.result[lhs] != context.result[rhs], 'Expected {} != {}'.format(lhs,rhs)



@then(u'A * identity_matrix = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A * identity_matrix = A')

@then(u'identity_matrix * a = a')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then identity_matrix * a = a')

@then(u'A = identity_matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A = identity_matrix')


@then(u'determinant(A) = 17')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 17')


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

@then(u'determinant(B) = 25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(B) = 25')


@then(u'determinant(A) = 0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 0')



@then(u'C * inverse(B) = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then C * inverse(B) = A')
    
@then(u'cofactor(A, 3, 2) = 105')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 3, 2) = 105')


@then(u'determinant(A) = 532')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 532')


@then(u'cofactor(A, 2, 3) = -160')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 2, 3) = -160')




@then(u'{matrix1:w} * {matrix2:w} is the following {rows:d}x{cols:d} matrix')
def step_impl(context,matrix1,matrix2,rows,cols):
    print(u'STEP: Then {} * {} is the following {}x{} matrix'.format(matrix1,matrix2,rows,cols))
    assert matrix1 in context.result, 'Expected {} to be available in context'.format(matrix1)
    assert matrix2 in context.result, 'Expected {} to be available in context'.format(matrix2)
    vals = [list(map(float,context.table.headings))]
    for row in context.table:
        vals += [list(map(float,row))]
    expectedResult = Matrix(rows,cols,vals)
    resultMatrix = context.result[matrix1] * context.result[matrix2]
    assert expectedResult == resultMatrix, 'Expected matrix result equals result matrix'


@then(u'A * {tuplevar:w} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context,tuplevar,x,y,z,w):
    matrixvar = 'A'
    print(u'STEP: Then {} * {} = tuple({}, {}, {}, {})'.format(matrixvar,tuplevar,x,y,z,w))
    assert matrixvar in context.result, 'Expected matrix {} to be available in context'.format(matrixvar)
    assert tuplevar  in context.result, 'Expected tuple {} to be available in context'.format(tuplevar)
    expected = Tuple(x,y,z,w)
    result = context.result[matrixvar].TimesTuple(context.result[tuplevar])
    assert expected == result, 'Expected {} == {}'.format(expected, result)


@then(u'transpose(A) is the following matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then transpose(A) is the following matrix')


@given(u'A ← transpose(identity_matrix)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A ← transpose(identity_matrix)')




@then(u'submatrix(A, 0, 2) is the following 2x2 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 0, 2) is the following 2x2 matrix')



@then(u'submatrix(A, 2, 1) is the following 3x3 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 2, 1) is the following 3x3 matrix')


@given(u'B ← submatrix(A, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← submatrix(A, 1, 0)')



@then(u'A is invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is invertible')

@then(u'A is not invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is not invertible')


@given(u'B ← inverse(A)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← inverse(A)')


#@then(u'B[3,2] = -160/532')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then B[3,2] = -160/532')


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
