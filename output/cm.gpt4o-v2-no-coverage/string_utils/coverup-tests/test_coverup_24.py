# file: string_utils/validation.py:418-431
# asked: {"lines": [418, 431], "branches": []}
# gained: {"lines": [418, 431], "branches": []}

import pytest
from string_utils.validation import is_ip_v6
from string_utils._regex import IP_V6_RE

def test_is_ip_v6_valid():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_is_ip_v6_invalid_character():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') == False

def test_is_ip_v6_empty_string():
    assert is_ip_v6('') == False

def test_is_ip_v6_none():
    assert is_ip_v6(None) == False

def test_is_ip_v6_spaces():
    assert is_ip_v6('    ') == False

def test_is_ip_v6_partial():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370') == False

def test_is_ip_v6_invalid_format():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334:1234') == False
