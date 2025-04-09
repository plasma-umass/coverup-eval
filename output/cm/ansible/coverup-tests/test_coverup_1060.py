# file lib/ansible/module_utils/facts/network/generic_bsd.py:197-198
# lines [197, 198]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_generic_bsd_ifconfig_network():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_lladdr_line(mock_generic_bsd_ifconfig_network):
    current_if = {}
    ips = []
    words = ['lladdr', '00:11:22:33:44:55']

    mock_generic_bsd_ifconfig_network.parse_lladdr_line(words, current_if, ips)

    assert 'lladdr' in current_if
    assert current_if['lladdr'] == '00:11:22:33:44:55'
