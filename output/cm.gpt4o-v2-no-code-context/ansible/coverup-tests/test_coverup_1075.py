# file: lib/ansible/module_utils/facts/network/generic_bsd.py:180-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    mock_module = mocker.Mock()
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_ether_line(network_instance):
    words = ['ether', '00:1a:2b:3c:4d:5e']
    current_if = {}
    ips = []

    network_instance.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == '00:1a:2b:3c:4d:5e'
    assert current_if['type'] == 'ether'
