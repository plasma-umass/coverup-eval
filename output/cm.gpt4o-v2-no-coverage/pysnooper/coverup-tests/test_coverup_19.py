# file: pysnooper/variables.py:13-17
# asked: {"lines": [13, 14, 15, 17], "branches": []}
# gained: {"lines": [13, 14, 15, 17], "branches": []}

import pytest

from pysnooper.variables import needs_parentheses

def test_needs_parentheses():
    # Test cases where parentheses are needed
    assert needs_parentheses('a + b') == True
    assert needs_parentheses('a * b + c') == True

    # Test cases where parentheses are not needed
    assert needs_parentheses('a') == False
    assert needs_parentheses('a_b') == False

    # Test cases with complex expressions
    assert needs_parentheses('(a + b)') == False
    assert needs_parentheses('(a * b)') == False

    # Test cases with function calls
    assert needs_parentheses('func(a, b)') == False
    assert needs_parentheses('(func(a + b))') == False

    # Test cases with attributes
    assert needs_parentheses('obj.attr') == False
    assert needs_parentheses('(obj).attr') == False

    # Test cases with indexing
    assert needs_parentheses('arr[0]') == False
    assert needs_parentheses('(arr)[0]') == False
