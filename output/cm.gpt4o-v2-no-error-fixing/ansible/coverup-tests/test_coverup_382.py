# file: lib/ansible/module_utils/common/network.py:144-149
# asked: {"lines": [144, 146, 147, 148, 149], "branches": [[147, 148], [147, 149]]}
# gained: {"lines": [144, 146, 147, 148, 149], "branches": [[147, 148], [147, 149]]}

import pytest

def test_to_bits():
    from ansible.module_utils.common.network import to_bits

    # Test with a standard netmask
    netmask = "255.255.255.0"
    expected_bits = "11111111111111111111111100000000"
    assert to_bits(netmask) == expected_bits

    # Test with another netmask
    netmask = "255.255.0.0"
    expected_bits = "11111111111111110000000000000000"
    assert to_bits(netmask) == expected_bits

    # Test with a different netmask
    netmask = "255.0.0.0"
    expected_bits = "11111111000000000000000000000000"
    assert to_bits(netmask) == expected_bits

    # Test with a netmask of all zeros
    netmask = "0.0.0.0"
    expected_bits = "00000000000000000000000000000000"
    assert to_bits(netmask) == expected_bits

    # Test with a netmask of all ones
    netmask = "255.255.255.255"
    expected_bits = "11111111111111111111111111111111"
    assert to_bits(netmask) == expected_bits
