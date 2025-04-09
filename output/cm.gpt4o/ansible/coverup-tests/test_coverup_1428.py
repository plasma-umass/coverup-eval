# file lib/ansible/module_utils/common/network.py:144-149
# lines [146, 147, 148, 149]
# branches ['147->148', '147->149']

import pytest
from ansible.module_utils.common.network import to_bits

def test_to_bits():
    # Test with a valid netmask
    netmask = '255.255.255.0'
    expected_bits = '11111111111111111111111100000000'
    assert to_bits(netmask) == expected_bits

    # Test with another valid netmask
    netmask = '255.255.0.0'
    expected_bits = '11111111111111110000000000000000'
    assert to_bits(netmask) == expected_bits

    # Test with a netmask with different octets
    netmask = '255.128.0.0'
    expected_bits = '11111111100000000000000000000000'
    assert to_bits(netmask) == expected_bits

    # Test with an invalid netmask to ensure it raises an error
    with pytest.raises(ValueError):
        to_bits('invalid.netmask')

    # Test with an empty string to ensure it raises an error
    with pytest.raises(ValueError):
        to_bits('')

    # Test with a netmask with non-numeric characters
    with pytest.raises(ValueError):
        to_bits('255.abc.0.0')
