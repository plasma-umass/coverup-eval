# file mimesis/providers/numbers.py:147-165
# lines [147, 148, 162, 163, 164, 165]
# branches []

import pytest
from mimesis.providers.numbers import Numbers
from mimesis.enums import NumTypes

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_matrix_with_integers(numbers_provider):
    m, n = 5, 5
    matrix = numbers_provider.matrix(m=m, n=n, num_type=NumTypes.INTEGERS)
    assert len(matrix) == m
    for row in matrix:
        assert len(row) == n
        for element in row:
            assert isinstance(element, int)

def test_matrix_with_floats(numbers_provider):
    m, n = 3, 4
    matrix = numbers_provider.matrix(m=m, n=n, num_type=NumTypes.FLOATS)
    assert len(matrix) == m
    for row in matrix:
        assert len(row) == n
        for element in row:
            assert isinstance(element, float)

def test_matrix_with_custom_type(numbers_provider, mocker):
    m, n = 2, 2
    custom_method_name = 'floats'
    custom_method = mocker.patch.object(numbers_provider, custom_method_name, return_value=[0.0] * n)
    matrix = numbers_provider.matrix(m=m, n=n, num_type=NumTypes.FLOATS)
    assert len(matrix) == m
    for row in matrix:
        assert len(row) == n
        for element in row:
            assert element == 0.0
    custom_method.assert_called_with(n=n)
