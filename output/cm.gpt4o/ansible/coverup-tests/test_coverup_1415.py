# file lib/ansible/inventory/manager.py:94-137
# lines [107, 109, 111, 116, 124, 128, 129, 134]
# branches ['106->107', '110->111', '115->116']

import pytest
from ansible.inventory.manager import split_host_pattern
from ansible.module_utils._text import to_text
import itertools
import re

def test_split_host_pattern(mocker):
    # Test case for pattern as a list
    pattern_list = ['a,b[1]', 'c[2:3] , d']
    expected_result = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern_list) == expected_result

    # Test case for pattern not being a string type
    pattern_non_string = b'a,b[1], c[2:3] , d'
    assert split_host_pattern(pattern_non_string) == expected_result

    # Test case for pattern with commas
    pattern_with_commas = 'a,b[1], c[2:3] , d'
    assert split_host_pattern(pattern_with_commas) == expected_result

    # Test case for pattern without commas but valid IPv6 address and host ranges
    pattern_ipv6 = 'a[1:2]:b[3:4]'
    mocker.patch('ansible.inventory.manager.parse_address', return_value=('a[1:2]', 'b[3:4]'))
    assert split_host_pattern(pattern_ipv6) == [pattern_ipv6]

    # Test case for pattern without commas and invalid IPv6 address and host ranges
    pattern_invalid_ipv6 = 'a:b:c'
    mocker.patch('ansible.inventory.manager.parse_address', side_effect=Exception)
    expected_result_invalid_ipv6 = ['a', 'b', 'c']
    assert split_host_pattern(pattern_invalid_ipv6) == expected_result_invalid_ipv6
