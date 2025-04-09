# file: pysnooper/variables.py:13-17
# asked: {"lines": [13, 14, 15, 17], "branches": []}
# gained: {"lines": [13, 14, 15, 17], "branches": []}

import pytest

from pysnooper.variables import needs_parentheses

def test_needs_parentheses_with_parentheses():
    assert needs_parentheses('a + b') == True

def test_needs_parentheses_without_parentheses():
    assert needs_parentheses('a') == False

def test_needs_parentheses_complex_expression():
    assert needs_parentheses('a + b * c') == True

def test_needs_parentheses_single_variable():
    assert needs_parentheses('variable') == False
