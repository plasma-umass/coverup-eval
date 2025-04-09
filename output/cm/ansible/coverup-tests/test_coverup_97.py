# file lib/ansible/module_utils/common/network.py:116-141
# lines [116, 120, 123, 124, 125, 126, 127, 128, 129, 132, 133, 134, 135, 136, 139, 140, 141]
# branches ['124->125', '124->128', '126->124', '126->127', '128->129', '128->132', '133->134', '133->139', '134->135', '134->136', '139->140', '139->141']

import pytest
from ansible.module_utils.common.network import to_ipv6_network

def test_to_ipv6_network():
    # Test with less than 3 groups before ::
    assert to_ipv6_network('2001::') == '2001::'
    # Test with exactly 3 groups before ::
    assert to_ipv6_network('2001:0db8:85a3::') == '2001:0db8:85a3::'
    # Test with more than 3 groups before ::
    assert to_ipv6_network('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == '2001:0db8:85a3::'
