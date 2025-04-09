# file: lib/ansible/utils/helpers.py:25-34
# asked: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}
# gained: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}

import pytest
from ansible.utils.helpers import pct_to_int

def test_pct_to_int_with_percentage():
    assert pct_to_int("50%", 200) == 100
    assert pct_to_int("0%", 200) == 1  # min_value should be returned

def test_pct_to_int_with_integer():
    assert pct_to_int(50, 200) == 50
    assert pct_to_int("50", 200) == 50

def test_pct_to_int_with_min_value():
    assert pct_to_int("0%", 200, min_value=5) == 5  # custom min_value should be returned

@pytest.mark.parametrize("value, num_items, min_value, expected", [
    ("25%", 400, 1, 100),
    ("100%", 400, 1, 400),
    ("0%", 400, 1, 1),
    ("0%", 400, 5, 5),
    (50, 400, 1, 50),
    ("50", 400, 1, 50),
])
def test_pct_to_int_parametrized(value, num_items, min_value, expected):
    assert pct_to_int(value, num_items, min_value) == expected
