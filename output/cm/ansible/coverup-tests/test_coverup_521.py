# file lib/ansible/module_utils/facts/network/sunos.py:106-111
# lines [106, 107, 108, 109, 110, 111]
# branches ['108->109', '108->111']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.sunos import SunOSNetwork

@pytest.fixture
def mock_interface():
    return {
        'device': 'mock0',
        'type': 'ether',
        'macaddress': None
    }

@pytest.fixture
def mock_ips():
    return []

def test_parse_ether_line(mock_interface, mock_ips):
    module_mock = MagicMock()
    sunos_network = SunOSNetwork(module=module_mock)
    words = ['ether', 'a1:b2:c3:d4:e5:f6']
    sunos_network.parse_ether_line(words, mock_interface, mock_ips)
    assert mock_interface['macaddress'] == 'a1:b2:c3:d4:e5:f6'
