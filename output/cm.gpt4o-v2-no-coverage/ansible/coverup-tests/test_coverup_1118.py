# file: lib/ansible/inventory/manager.py:94-137
# asked: {"lines": [106, 107, 109, 110, 111, 115, 116, 121, 122, 123, 124, 128, 129, 134, 137], "branches": [[106, 107], [106, 110], [110, 111], [110, 115], [115, 116], [115, 121]]}
# gained: {"lines": [106, 107, 109, 110, 111, 115, 116, 121, 122, 124, 128, 129, 134, 137], "branches": [[106, 107], [106, 110], [110, 111], [110, 115], [115, 116], [115, 121]]}

import pytest
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text
from ansible.parsing.utils.addresses import parse_address
from ansible.inventory.manager import split_host_pattern

def test_split_host_pattern_with_comma():
    pattern = 'a,b[1], c[2:3] , d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_colon():
    pattern = 'a:b[1]: c[2:3] : d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_list():
    pattern = ['a,b[1]', ' c[2:3] , d']
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_non_string():
    pattern = b'a,b[1], c[2:3] , d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_ipv6():
    pattern = 'a,b[1], c[2:3] , d, [2001:db8::1]'
    expected = ['a', 'b[1]', 'c[2:3]', 'd', '[2001:db8::1]']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_invalid_pattern():
    pattern = 'a,b[1], c[2:3] , d, [2001:db8::1]:80'
    expected = ['a', 'b[1]', 'c[2:3]', 'd', '[2001:db8::1]:80']
    result = split_host_pattern(pattern)
    assert result == expected
