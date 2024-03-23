# file py_backwards/utils/helpers.py:20-29
# lines [20, 21, 23, 24, 26, 27, 29]
# branches []

import pytest
from py_backwards.utils.helpers import VariablesGenerator

def test_variables_generator():
    initial_counter = VariablesGenerator._counter
    generated_variable = VariablesGenerator.generate('testvar')
    expected_variable = '_py_backwards_testvar_{}'.format(initial_counter)
    
    assert generated_variable == expected_variable
    assert VariablesGenerator._counter == initial_counter + 1

    # Clean up by resetting the counter to its initial value
    VariablesGenerator._counter = initial_counter
