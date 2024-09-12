# file: lib/ansible/module_utils/facts/network/generic_bsd.py:176-178
# asked: {"lines": [176, 178], "branches": []}
# gained: {"lines": [176, 178], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    module_mock = mocker.Mock()
    return GenericBsdIfconfigNetwork(module=module_mock)

def test_parse_nd6_line(network_instance, mocker):
    words = ["nd6", "option_string"]
    current_if = {}
    ips = []

    mock_get_options = mocker.patch.object(network_instance, 'get_options', return_value="parsed_options")

    network_instance.parse_nd6_line(words, current_if, ips)

    mock_get_options.assert_called_once_with("option_string")
    assert current_if['options'] == "parsed_options"
