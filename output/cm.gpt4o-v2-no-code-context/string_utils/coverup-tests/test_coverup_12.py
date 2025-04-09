# file: string_utils/validation.py:434-448
# asked: {"lines": [434, 448], "branches": []}
# gained: {"lines": [434, 448], "branches": []}

import pytest
from string_utils.validation import is_ip

def test_is_ip_v4_valid():
    assert is_ip('255.200.100.75') == True

def test_is_ip_v6_valid():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_is_ip_invalid():
    assert is_ip('1.2.3') == False

def test_is_ip_non_ip_string():
    assert is_ip('not.an.ip.address') == False

def test_is_ip_empty_string():
    assert is_ip('') == False

def test_is_ip_none():
    assert is_ip(None) == False

def test_is_ip_integer():
    assert is_ip(12345) == False

def test_is_ip_special_characters():
    assert is_ip('!@#$%^&*()') == False
