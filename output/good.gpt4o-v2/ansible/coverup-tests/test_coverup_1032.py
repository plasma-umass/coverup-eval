# file: lib/ansible/module_utils/facts/network/generic_bsd.py:172-174
# asked: {"lines": [172, 174], "branches": []}
# gained: {"lines": [172, 174], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    module_mock = mocker.Mock()
    return GenericBsdIfconfigNetwork(module=module_mock)

def test_parse_options_line(network_instance, mocker):
    words = ["option1"]
    current_if = {}
    ips = []

    mock_get_options = mocker.patch.object(network_instance, 'get_options', return_value="mocked_options")

    network_instance.parse_options_line(words, current_if, ips)

    assert 'options' in current_if
    assert current_if['options'] == "mocked_options"
    mock_get_options.assert_called_once_with("option1")
