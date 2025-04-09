# file: lib/ansible/module_utils/common/network.py:86-113
# asked: {"lines": [86, 92, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 111, 112, 113], "branches": [[96, 97], [96, 100], [98, 96], [98, 99], [100, 101], [100, 104], [105, 106], [105, 111], [106, 107], [106, 108], [111, 112], [111, 113]]}
# gained: {"lines": [86, 92, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 111, 112, 113], "branches": [[96, 97], [96, 100], [98, 96], [98, 99], [100, 101], [100, 104], [105, 106], [105, 111], [106, 107], [106, 108], [111, 112], [111, 113]]}

import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

def test_to_ipv6_subnet_full_address():
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3:0000::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_partial_address():
    addr = "2001:0db8:85a3::8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_shortened_address():
    addr = "2001:db8::"
    expected = "2001:db8::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_not_enough_groups():
    addr = "2001:db8:85a3"
    expected = "2001:db8:85a3::"
    result = to_ipv6_subnet(addr)
    assert result == expected

def test_to_ipv6_subnet_empty_address():
    addr = ""
    expected = "::"
    result = to_ipv6_subnet(addr)
    assert result == expected
