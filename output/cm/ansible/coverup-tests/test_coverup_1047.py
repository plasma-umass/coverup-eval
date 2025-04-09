# file lib/ansible/module_utils/facts/network/generic_bsd.py:172-174
# lines [172, 174]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_generic_bsd_ifconfig_network():
    module = MagicMock()
    network = GenericBsdIfconfigNetwork(module)
    network.get_options = MagicMock(return_value='mocked_options')
    return network

def test_parse_options_line(mock_generic_bsd_ifconfig_network):
    current_if = {}
    ips = []
    words = ['options']

    mock_generic_bsd_ifconfig_network.parse_options_line(words, current_if, ips)

    assert 'options' in current_if
    assert current_if['options'] == 'mocked_options'
