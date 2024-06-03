# file lib/ansible/module_utils/facts/network/generic_bsd.py:176-178
# lines [178]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

@pytest.fixture
def network(mocker):
    # Mock the module argument required by Network's __init__ method
    mock_module = mocker.Mock()
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_nd6_line_executes_line_178(network, mocker):
    # Mock the get_options method to ensure it gets called
    mock_get_options = mocker.patch.object(network, 'get_options', return_value='mocked_options')

    words = ['nd6', 'option1']
    current_if = {}
    ips = []

    network.parse_nd6_line(words, current_if, ips)

    # Assert that get_options was called with the correct argument
    mock_get_options.assert_called_once_with('option1')
    # Assert that current_if['options'] is set correctly
    assert current_if['options'] == 'mocked_options'
