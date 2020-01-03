#! python
#
# Steps for matrix tests
#
from behave import given, then
from renderer.matrix import Matrix, IdentityMatrix
from renderer.bolts  import Tuple
from math import isclose

def buildMatrixFromContextTable(context,rows=None,cols=None):
    vals = [list(map(float,context.table.headings))]
    for row in context.table:
        vals += [list(map(float,row))]
    if rows is None:
        rows = len(vals)
    if cols is None:
        cols = len(vals[0])
    assert rows == len(vals)
    for row in vals:
        assert cols == len(row)
    return Matrix(rows,cols,vals)

@given(u'the following {rows:d}x{cols:d} matrix {matrixvar:w}')
def step_impl(context, rows, cols, matrixvar):
    print(u'STEP: Given the following {}x{} matrix {}'.format(rows,cols,matrixvar))
    if 'result' not in context:
        context.result = {}
    #print(vals)
    context.result[matrixvar] = buildMatrixFromContextTable(context,rows,cols)
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
    context.result[matrixvar] = buildMatrixFromContextTable(context)
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
    print(u'STEP: Then A * identity_matrix = A')
    matrixvar = 'A'
    assert matrixvar in context.result, 'Expected Matrix {} to be in context'.format(matrixvar)
    result = context.result[matrixvar] * IdentityMatrix
    assert context.result[matrixvar] == result, 'Expect multiplying {} by the identity_matrix matches {}'.format(matrixvar,matrixvar)

@then(u'identity_matrix * a = a')
def step_impl(context):
    print(u'STEP: Then identity_matrix * a = a')
    tuplevar = 'a'
    assert tuplevar in context.result, 'Expected Tuple {} to be in context'.format(tuplevar)
    result = IdentityMatrix.TimesTuple(context.result[tuplevar])
    assert context.result[tuplevar] == result, 'Expect multiplying the identity_matrix by tuple {} matches {}'.format(tuplevar, tuplevar)

@then(u'{matrixvar:w} = identity_matrix')
def step_impl(context, matrixvar):
    print(u'STEP: Then {} = identity_matrix'.format(matrixvar))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    assert context.result[matrixvar] == IdentityMatrix, 'Expected Matrix {} to be equal to the identity_matrix'.format(matrixvar)
    #raise NotImplementedError(u'STEP: Then A = identity_matrix')


@then(u'determinant({matrixvar:w}) = {val:g}')
def step_impl(context, matrixvar, val):
    print(u'STEP: Then determinant({}) = {}'.format(matrixvar,val))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    result = context.result[matrixvar].Determinant()
    assert val == result, 'Expected Determinant({}) = {}, found it equal to {}'.format(matrixvar, val, result)
    #raise NotImplementedError(u'STEP: Then determinant(A) = 17')


@then(u'minor({matrixvar:w}, {row:d}, {column:d}) = {val:g}')
def step_impl(context,matrixvar,row,column,val):
    print(u'STEP: Then minor({}, {}, {}) = {}'.format(matrixvar,row,column,val))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    result = context.result[matrixvar].Minor(row, column)
    assert val == result, 'Expected Minor({}, {}, {}) = {}, found it equal to {}'.format(matrixvar, row, column, val, result)




@then(u'cofactor({matrixvar:w}, {row:d}, {column:d}) = {val:g}')
def step_impl(context,matrixvar,row,column,val):
    print(u'STEP: Then cofactor({}, {}, {}) = {}'.format(matrixvar,row,column,val))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    result = context.result[matrixvar].Cofactor(row, column)
    assert val == result, 'Expected Cofactor({}, {}, {}) = {}, found it equal to {}'.format(matrixvar, row, column, val, result)
    #raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = -12')








@then(u'C * inverse(B) = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then C * inverse(B) = A')





@then(u'{matrix1:w} * {matrix2:w} is the following {rows:d}x{cols:d} matrix')
def step_impl(context,matrix1,matrix2,rows,cols):
    print(u'STEP: Then {} * {} is the following {}x{} matrix'.format(matrix1,matrix2,rows,cols))
    assert matrix1 in context.result, 'Expected {} to be available in context'.format(matrix1)
    assert matrix2 in context.result, 'Expected {} to be available in context'.format(matrix2)
    expectedResult = buildMatrixFromContextTable(context,rows,cols)
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


@then(u'transpose({matrixvar:w}) is the following matrix')
def step_impl(context,matrixvar):
    print(u'STEP: Then transpose({}) is the following matrix'.format(matrixvar))
    assert matrixvar in context.result, 'Expected matrix {} to be available in context'.format(matrixvar)
    expected = buildMatrixFromContextTable(context)
    resultMatrix = context.result[matrixvar].Transpose()
    assert expected == resultMatrix, 'Expected transpose({}) to be equal to provided matrix'.format(matrixvar)


@given(u'{matrixvar:w} ← transpose(identity_matrix)')
def step_impl(context, matrixvar):
    print(u'STEP: Given {} ← transpose(identity_matrix)'.format(matrixvar))
    if 'result' not in context:
        context.result = {}
    context.result[matrixvar] = IdentityMatrix.Transpose()
    pass


@then(u'submatrix({matrixvar:w}, {row:d}, {column:d}) is the following {rows:d}x{columns:d} matrix')
def step_impl(context, matrixvar, row, column, rows, columns):
    print(u'STEP: Then submatrix({}, {}, {}) is the following {}x{} matrix'.format(matrixvar, row, column, rows, columns))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    result = context.result[matrixvar].Submatrix(row,column)
    expected = buildMatrixFromContextTable(context, rows, columns)
    assert expected == result, 'Expected submatrix({}, {}, {}) to be equal to provided matrix'.format(matrixvar, row, column)


@given(u'{destmatrix:w} ← submatrix({sourcematrix:w}, {row:d}, {column:d})')
def step_impl(context,destmatrix,sourcematrix,row,column):
    print(u'STEP: Given {} ← submatrix({}, {}, {})'.format(destmatrix,sourcematrix,row,column))
    assert sourcematrix in context.result, 'Expected Matrix {} to be available in context'.format(sourcematrix)
    context.result[destmatrix] = context.result[sourcematrix].Submatrix(row,column)
    pass



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
