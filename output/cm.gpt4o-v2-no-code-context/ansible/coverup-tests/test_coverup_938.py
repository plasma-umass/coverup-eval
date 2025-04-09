# file: lib/ansible/module_utils/common/network.py:116-141
# asked: {"lines": [120, 123, 124, 125, 126, 127, 128, 129, 132, 133, 134, 135, 136, 139, 140, 141], "branches": [[124, 125], [124, 128], [126, 124], [126, 127], [128, 129], [128, 132], [133, 134], [133, 139], [134, 135], [134, 136], [139, 140], [139, 141]]}
# gained: {"lines": [120, 123, 124, 125, 126, 127, 128, 129, 132, 133, 134, 135, 136, 139, 140, 141], "branches": [[124, 125], [124, 128], [126, 124], [126, 127], [128, 129], [128, 132], [133, 134], [133, 139], [134, 135], [134, 136], [139, 140], [139, 141]]}

import pytest

from ansible.module_utils.common.network import to_ipv6_network

def test_to_ipv6_network_full_address():
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    result = to_ipv6_network(addr)
    assert result == expected

def test_to_ipv6_network_shortened_address():
    addr = "2001:0db8:85a3::8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    result = to_ipv6_network(addr)
    assert result == expected

def test_to_ipv6_network_two_groups():
    addr = "2001:0db8::8a2e:0370:7334"
    expected = "2001:0db8::"
    result = to_ipv6_network(addr)
    assert result == expected

def test_to_ipv6_network_one_group():
    addr = "2001::8a2e:0370:7334"
    expected = "2001::"
    result = to_ipv6_network(addr)
    assert result == expected

def test_to_ipv6_network_no_groups():
    addr = "::8a2e:0370:7334"
    expected = "::"
    result = to_ipv6_network(addr)
    assert result == expected
