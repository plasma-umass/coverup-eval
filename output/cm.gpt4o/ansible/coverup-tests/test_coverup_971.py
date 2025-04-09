# file lib/ansible/module_utils/facts/network/generic_bsd.py:172-174
# lines [172, 174]
# branches []

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance():
    module = Mock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_options_line(network_instance, mocker):
    words = ['options=some_option']
    current_if = {}
    ips = []

    mock_get_options = mocker.patch.object(network_instance, 'get_options', return_value='some_option')

    network_instance.parse_options_line(words, current_if, ips)

    mock_get_options.assert_called_once_with('options=some_option')
    assert current_if['options'] == 'some_option'
