# file: pysnooper/variables.py:13-17
# asked: {"lines": [13, 14, 15, 17], "branches": []}
# gained: {"lines": [13, 14, 15, 17], "branches": []}

import pytest

from pysnooper.variables import needs_parentheses

def test_needs_parentheses_no_parentheses():
    assert not needs_parentheses('a')

def test_needs_parentheses_with_parentheses():
    assert needs_parentheses('a + b')

def test_needs_parentheses_complex_expression():
    assert needs_parentheses('a + b * c')

def test_needs_parentheses_function_call():
    assert not needs_parentheses('func(a)')

def test_needs_parentheses_attribute_access():
    assert not needs_parentheses('a.b')
