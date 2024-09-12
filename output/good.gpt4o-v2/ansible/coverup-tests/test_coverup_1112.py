# file: lib/ansible/module_utils/common/network.py:86-113
# asked: {"lines": [92, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 111, 112, 113], "branches": [[96, 97], [96, 100], [98, 96], [98, 99], [100, 101], [100, 104], [105, 106], [105, 111], [106, 107], [106, 108], [111, 112], [111, 113]]}
# gained: {"lines": [92, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 111, 112, 113], "branches": [[96, 97], [96, 100], [98, 96], [98, 99], [100, 101], [100, 104], [105, 106], [105, 111], [106, 107], [106, 108], [111, 112], [111, 113]]}

import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

def test_to_ipv6_subnet_full_groups():
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3:0000::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_partial_groups():
    addr = "2001:0db8:85a3::8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_less_than_four_groups():
    addr = "2001:0db8::"
    expected = "2001:0db8::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_exactly_four_groups():
    addr = "2001:0db8:85a3:0000::"
    expected = "2001:0db8:85a3:0000::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_not_ending_with_double_colon():
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3:0000::"
    result = to_ipv6_subnet(addr)
    assert result == expected
