# file: py_backwards/utils/helpers.py:20-29
# asked: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}
# gained: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}

import pytest
from py_backwards.utils.helpers import VariablesGenerator

@pytest.fixture(autouse=True)
def reset_counter():
    # Reset the counter before each test to avoid state pollution
    VariablesGenerator._counter = 0
    yield
    VariablesGenerator._counter = 0

def test_generate_unique_variable():
    var1 = VariablesGenerator.generate('test')
    var2 = VariablesGenerator.generate('test')
    var3 = VariablesGenerator.generate('another_test')

    assert var1 == '_py_backwards_test_0'
    assert var2 == '_py_backwards_test_1'
    assert var3 == '_py_backwards_another_test_2'

def test_generate_with_different_variables():
    var1 = VariablesGenerator.generate('foo')
    var2 = VariablesGenerator.generate('bar')

    assert var1 == '_py_backwards_foo_0'
    assert var2 == '_py_backwards_bar_1'
