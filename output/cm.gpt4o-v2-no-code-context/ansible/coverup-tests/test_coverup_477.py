# file: lib/ansible/utils/helpers.py:25-34
# asked: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}
# gained: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}

import pytest
from ansible.utils.helpers import pct_to_int

def test_pct_to_int_with_percentage_string():
    result = pct_to_int("50%", 200)
    assert result == 100

def test_pct_to_int_with_percentage_string_min_value():
    result = pct_to_int("0%", 200)
    assert result == 1

def test_pct_to_int_with_integer_string():
    result = pct_to_int("42", 200)
    assert result == 42

def test_pct_to_int_with_integer():
    result = pct_to_int(42, 200)
    assert result == 42
