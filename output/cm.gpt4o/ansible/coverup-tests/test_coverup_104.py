# file lib/ansible/module_utils/common/network.py:116-141
# lines [116, 120, 123, 124, 125, 126, 127, 128, 129, 132, 133, 134, 135, 136, 139, 140, 141]
# branches ['124->125', '124->128', '126->124', '126->127', '128->129', '128->132', '133->134', '133->139', '134->135', '134->136', '139->140', '139->141']

import pytest
from ansible.module_utils.common.network import to_ipv6_network

def test_to_ipv6_network():
    # Test case 1: Full IPv6 address
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected

    # Test case 2: IPv6 address with omitted zeros
    addr = "2001:0db8:85a3::8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected

    # Test case 3: IPv6 address with less than three groups
    addr = "2001:0db8::"
    expected = "2001:0db8::"
    assert to_ipv6_network(addr) == expected

    # Test case 4: IPv6 address with exactly three groups
    addr = "2001:0db8:85a3::"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected

    # Test case 5: IPv6 address with more than three groups
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected

    # Test case 6: IPv6 address with exactly three groups and no omitted zeros
    addr = "2001:0db8:85a3::"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected

    # Test case 7: IPv6 address with less than three groups and no omitted zeros
    addr = "2001:0db8::"
    expected = "2001:0db8::"
    assert to_ipv6_network(addr) == expected

    # Test case 8: IPv6 address with more than three groups and no omitted zeros
    addr = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    expected = "2001:0db8:85a3::"
    assert to_ipv6_network(addr) == expected
