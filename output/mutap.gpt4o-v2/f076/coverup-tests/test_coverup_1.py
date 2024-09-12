# file: f076/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest
from f076 import is_simple_power

def test_is_simple_power_n_equals_1():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(2, 1) == False

def test_is_simple_power_general_case():
    assert is_simple_power(8, 2) == True
    assert is_simple_power(9, 2) == False
    assert is_simple_power(27, 3) == True
    assert is_simple_power(28, 3) == False

def test_is_simple_power_edge_cases():
    assert is_simple_power(0, 2) == False
    assert is_simple_power(1, 2) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(3, 2) == False
