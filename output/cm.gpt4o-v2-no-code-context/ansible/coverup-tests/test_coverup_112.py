# file: lib/ansible/inventory/manager.py:94-137
# asked: {"lines": [94, 106, 107, 109, 110, 111, 115, 116, 121, 122, 123, 124, 128, 129, 134, 137], "branches": [[106, 107], [106, 110], [110, 111], [110, 115], [115, 116], [115, 121]]}
# gained: {"lines": [94, 106, 107, 109, 110, 111, 115, 116, 121, 122, 124, 128, 129, 134, 137], "branches": [[106, 107], [106, 110], [110, 111], [110, 115], [115, 116], [115, 121]]}

import pytest
from ansible.inventory.manager import split_host_pattern
from ansible.module_utils._text import to_text
from ansible.module_utils.six import string_types
import itertools
import re

def test_split_host_pattern_with_comma():
    pattern = 'a,b[1], c[2:3] , d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_list():
    pattern = ['a,b[1]', 'c[2:3] , d']
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_non_string():
    pattern = b'a,b[1], c[2:3] , d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_colon():
    pattern = 'a:b[1]:c[2:3]:d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_ipv6():
    pattern = 'a, b[1], c[2:3], d, [fe80::1]'
    expected = ['a', 'b[1]', 'c[2:3]', 'd', '[fe80::1]']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_invalid_colon():
    pattern = 'a:b[1]:c[2:3]:d:invalid:pattern'
    expected = ['a', 'b[1]', 'c[2:3]', 'd', 'invalid', 'pattern']
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_empty_string():
    pattern = ''
    expected = []
    result = split_host_pattern(pattern)
    assert result == expected

def test_split_host_pattern_with_whitespace():
    pattern = '   '
    expected = []
    result = split_host_pattern(pattern)
    assert result == expected
