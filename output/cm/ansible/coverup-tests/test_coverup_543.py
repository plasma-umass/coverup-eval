# file lib/ansible/utils/helpers.py:25-34
# lines [25, 30, 31, 32, 34]
# branches ['30->31', '30->34']

import pytest
from ansible.utils.helpers import pct_to_int

def test_pct_to_int_percentage():
    num_items = 100
    percentage_value = "50%"
    expected_value = 50
    assert pct_to_int(percentage_value, num_items) == expected_value

def test_pct_to_int_percentage_with_min_value():
    num_items = 100
    percentage_value = "0%"
    min_value = 10
    expected_value = min_value
    assert pct_to_int(percentage_value, num_items, min_value) == expected_value

def test_pct_to_int_integer():
    num_items = 100
    integer_value = 30
    expected_value = 30
    assert pct_to_int(integer_value, num_items) == expected_value

def test_pct_to_int_integer_with_min_value():
    num_items = 100
    integer_value = "0%"
    min_value = 5
    expected_value = min_value
    assert pct_to_int(integer_value, num_items, min_value) == expected_value
