# file lib/ansible/module_utils/common/network.py:144-149
# lines [144, 146, 147, 148, 149]
# branches ['147->148', '147->149']

import pytest
from ansible.module_utils.common.network import to_bits

def test_to_bits():
    # Test with a full netmask
    assert to_bits('255.255.255.255') == '11111111111111111111111111111111', "to_bits should convert full netmask to bits"

    # Test with a partial netmask
    assert to_bits('255.255.255.0') == '11111111111111111111111100000000', "to_bits should convert partial netmask to bits"

    # Test with a zero netmask
    assert to_bits('0.0.0.0') == '00000000000000000000000000000000', "to_bits should convert zero netmask to bits"

    # Test with a non-standard netmask
    assert to_bits('255.224.0.0') == '11111111111000000000000000000000', "to_bits should convert non-standard netmask to bits"

# Note: No cleanup is necessary for this test as it does not affect external state or other tests.
