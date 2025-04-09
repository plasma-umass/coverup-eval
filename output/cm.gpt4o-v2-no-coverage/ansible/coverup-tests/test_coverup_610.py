# file: lib/ansible/module_utils/common/network.py:144-149
# asked: {"lines": [144, 146, 147, 148, 149], "branches": [[147, 148], [147, 149]]}
# gained: {"lines": [144, 146, 147, 148, 149], "branches": [[147, 148], [147, 149]]}

import pytest

from ansible.module_utils.common.network import to_bits

def test_to_bits():
    # Test with a standard netmask
    assert to_bits('255.255.255.0') == '11111111111111111111111100000000'
    
    # Test with another netmask
    assert to_bits('255.255.0.0') == '11111111111111110000000000000000'
    
    # Test with a different netmask
    assert to_bits('255.0.0.0') == '11111111000000000000000000000000'
    
    # Test with a netmask with different values
    assert to_bits('255.128.0.0') == '11111111100000000000000000000000'
    
    # Test with a netmask with all zeros
    assert to_bits('0.0.0.0') == '00000000000000000000000000000000'
    
    # Test with a netmask with mixed values
    assert to_bits('255.255.255.128') == '11111111111111111111111110000000'
