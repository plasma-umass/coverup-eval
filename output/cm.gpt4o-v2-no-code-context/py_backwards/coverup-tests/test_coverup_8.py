# file: py_backwards/utils/helpers.py:20-29
# asked: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}
# gained: {"lines": [20, 21, 23, 24, 26, 27, 29], "branches": []}

import pytest
from py_backwards.utils.helpers import VariablesGenerator

def test_generate_unique_variable_name():
    # Reset the counter to ensure clean state
    VariablesGenerator._counter = 0
    
    var1 = VariablesGenerator.generate('test')
    var2 = VariablesGenerator.generate('test')
    
    assert var1 == '_py_backwards_test_0'
    assert var2 == '_py_backwards_test_1'
    assert VariablesGenerator._counter == 2

def test_generate_with_different_variables():
    # Reset the counter to ensure clean state
    VariablesGenerator._counter = 0
    
    var1 = VariablesGenerator.generate('var1')
    var2 = VariablesGenerator.generate('var2')
    
    assert var1 == '_py_backwards_var1_0'
    assert var2 == '_py_backwards_var2_1'
    assert VariablesGenerator._counter == 2
