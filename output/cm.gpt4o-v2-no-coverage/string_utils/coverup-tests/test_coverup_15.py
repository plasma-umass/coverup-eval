# file: string_utils/validation.py:434-448
# asked: {"lines": [434, 448], "branches": []}
# gained: {"lines": [434, 448], "branches": []}

import pytest
from string_utils.validation import is_ip

def test_is_ip_v4_valid():
    assert is_ip('255.200.100.75') == True

def test_is_ip_v4_invalid():
    assert is_ip('255.200.100.999') == False

def test_is_ip_v6_valid():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_is_ip_v6_invalid():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:?') == False

def test_is_ip_invalid_format():
    assert is_ip('1.2.3') == False
