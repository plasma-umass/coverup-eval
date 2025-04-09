# file lib/ansible/module_utils/facts/network/generic_bsd.py:176-178
# lines [176, 178]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_generic_bsd_ifconfig_network():
    module = MagicMock()
    network = GenericBsdIfconfigNetwork(module)
    network.get_options = MagicMock(return_value=['option1', 'option2'])
    return network

def test_parse_nd6_line(mock_generic_bsd_ifconfig_network):
    current_if = {}
    ips = []
    words = ['nd6', 'options=1<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>']

    mock_generic_bsd_ifconfig_network.parse_nd6_line(words, current_if, ips)

    assert 'options' in current_if
    assert current_if['options'] == ['option1', 'option2']
    mock_generic_bsd_ifconfig_network.get_options.assert_called_once_with(words[1])
