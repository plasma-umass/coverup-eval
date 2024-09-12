# file: lib/ansible/utils/helpers.py:25-34
# asked: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}
# gained: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}

import pytest
from ansible.utils.helpers import pct_to_int

def test_pct_to_int_with_percentage(monkeypatch):
    # Test with percentage value
    result = pct_to_int("50%", 100)
    assert result == 50

def test_pct_to_int_with_percentage_min_value(monkeypatch):
    # Test with percentage value resulting in less than min_value
    result = pct_to_int("0%", 100)
    assert result == 1

def test_pct_to_int_with_integer(monkeypatch):
    # Test with integer value
    result = pct_to_int("10", 100)
    assert result == 10

def test_pct_to_int_with_integer_min_value(monkeypatch):
    # Test with integer value less than min_value
    result = pct_to_int("0", 100)
    assert result == 0
