# file lib/ansible/module_utils/facts/network/generic_bsd.py:194-195
# lines [194, 195]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_generic_bsd_ifconfig_network():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module=module)

def test_parse_status_line(mock_generic_bsd_ifconfig_network):
    current_if = {}
    ips = []
    words = ['status:', 'active']
    
    mock_generic_bsd_ifconfig_network.parse_status_line(words, current_if, ips)
    
    assert 'status' in current_if
    assert current_if['status'] == 'active'
