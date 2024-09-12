# file: string_utils/validation.py:418-431
# asked: {"lines": [418, 431], "branches": []}
# gained: {"lines": [418, 431], "branches": []}

import pytest
from string_utils.validation import is_ip_v6

def test_is_ip_v6_valid():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_is_ip_v6_invalid_character():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') == False

def test_is_ip_v6_empty_string():
    assert is_ip_v6('') == False

def test_is_ip_v6_non_string_input():
    assert is_ip_v6(12345) == False
    assert is_ip_v6(None) == False
    assert is_ip_v6([]) == False
    assert is_ip_v6({}) == False

def test_is_ip_v6_partial_string(monkeypatch):
    def mock_is_full_string(input_string):
        return False
    monkeypatch.setattr('string_utils.validation.is_full_string', mock_is_full_string)
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == False
