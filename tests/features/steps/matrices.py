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


@then(u'determinant({matrixvar:w}) = {val:g}')
def step_impl(context, matrixvar, val):
    print(u'STEP: Then determinant({}) = {}'.format(matrixvar,val))
    assert matrixvar in context.result, 'Expected Matrix {} to be available in context'.format(matrixvar)
    result = context.result[matrixvar].Determinant()
    assert val == result, 'Expected Determinant({}) = {}, found it equal to {}'.format(matrixvar, val, result)


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


@then(u'{matrixvar:w} is invertible')
def step_impl(context, matrixvar):
    print(u'STEP: Then {} is invertible'.format(matrixvar))
    assert matrixvar in context.result
    assert context.result[matrixvar].IsInvertible(), 'Expected Matrix {} to be invertible, but it is not'.format(matrixvar)


@then(u'{matrixvar:w} is not invertible')
def step_impl(context,matrixvar):
    print(u'STEP: Then {} is not invertible'.format(matrixvar))
    assert matrixvar in context.result
    assert not context.result[matrixvar].IsInvertible(), 'Expected Matrix {} is not invertible, but it is'.format(matrixvar)


@given(u'{destmatrix:w} ← inverse({sourcematrix:w})')
def step_impl(context, destmatrix, sourcematrix):
    print(u'STEP: Given B ← inverse(A)'.format(destmatrix,sourcematrix))
    assert sourcematrix in context.result
    context.result[destmatrix] = context.result[sourcematrix].Inverse()
    pass


@then(u'{matrixvar:w}[{row:d},{col:d}] = {numerator:g}/{denominator:g}')
def step_impl(context,matrixvar,row,col,numerator,denominator):
    print(u'STEP: Then {}[{},{}] = {}/{}'.format(matrixvar,row,col,numerator,denominator))
    assert matrixvar in context.result
    expected = numerator / denominator
    result   = context.result[matrixvar][row,col]
    assert isclose(expected,result), 'Expected {} to be value at {}[{},{}], but found {}'.format(expected, matrixvar, row, col, result)


@then(u'{matrixvar:w} is the following {rows:d}x{columns:d} matrix')
def step_impl(context, matrixvar, rows, columns):
    print(u'STEP: Then {} is the following {}x{} matrix'.format(matrixvar, rows, columns))
    assert matrixvar in context.result
    expected = buildMatrixFromContextTable(context, rows, columns)
    assert context.result[matrixvar].Compare(expected), 'Expected {} to be equal to the provided matrix'.format(matrixvar)


@then(u'inverse({matrixvar:w}) is the following {rows:d}x{columns:d} matrix')
def step_impl(context, matrixvar, rows, columns):
    print(u'STEP: Then inverse(A) is the following 4x4 matrix'.format(matrixvar, rows, columns))
    assert matrixvar in context.result
    expected = buildMatrixFromContextTable(context, rows, columns)
    assert context.result[matrixvar].Inverse().Compare(expected), 'Expected inverse({}) to be equal to the provided matrix'.format(matrixvar)


@given(u'C ← A * B')
def step_impl(context):
    print(u'STEP: Given C ← A * B')
    assert 'B' in context.result
    assert 'A' in context.result
    context.result['C'] = context.result['A'] * context.result['B']
    pass


@then(u'{matrix1:w} * inverse({matrix2:w}) = {matrix3:w}')
def step_impl(context, matrix1, matrix2, matrix3):
    print(u'STEP: Then {} * inverse({}) = {}'.format(matrix1,matrix2,matrix3))
    assert matrix1 in context.result
    assert matrix2 in context.result
    assert matrix3 in context.result
    result = context.result[matrix1] * context.result[matrix2].Inverse()
    assert result.Compare(context.result[matrix3]), 'Expected {} * inverse({}) = {}, but it does not'.format(matrix1, matrix2, matrix3)
