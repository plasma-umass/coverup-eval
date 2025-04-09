# file: py_backwards/utils/helpers.py:20-29
# asked: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}
# gained: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}

import pytest
from py_backwards.utils.helpers import VariablesGenerator

def test_generate_unique_variable_names():
    # Reset the counter before the test
    VariablesGenerator._counter = 0

    var1 = VariablesGenerator.generate("test")
    assert var1 == "_py_backwards_test_0"
    assert VariablesGenerator._counter == 1

    var2 = VariablesGenerator.generate("test")
    assert var2 == "_py_backwards_test_1"
    assert VariablesGenerator._counter == 2

    var3 = VariablesGenerator.generate("example")
    assert var3 == "_py_backwards_example_2"
    assert VariablesGenerator._counter == 3

    # Clean up by resetting the counter after the test
    VariablesGenerator._counter = 0
