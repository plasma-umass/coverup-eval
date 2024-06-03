# file py_backwards/utils/helpers.py:20-29
# lines [20, 21, 23, 24, 26, 27, 29]
# branches []

import pytest
from py_backwards.utils.helpers import VariablesGenerator

def test_generate_unique_variable_name():
    # Ensure the counter starts at 0
    VariablesGenerator._counter = 0
    
    var1 = VariablesGenerator.generate('test')
    var2 = VariablesGenerator.generate('test')
    
    assert var1 == '_py_backwards_test_0'
    assert var2 == '_py_backwards_test_1'
    
    # Ensure the counter has incremented correctly
    assert VariablesGenerator._counter == 2
