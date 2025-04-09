# file: lib/ansible/module_utils/facts/network/generic_bsd.py:180-182
# asked: {"lines": [180, 181, 182], "branches": []}
# gained: {"lines": [180, 181, 182], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    module_mock = mocker.Mock()
    return GenericBsdIfconfigNetwork(module=module_mock)

def test_parse_ether_line(network_instance):
    words = ["ether", "00:1A:2B:3C:4D:5E"]
    current_if = {}
    ips = []

    network_instance.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == "00:1A:2B:3C:4D:5E"
    assert current_if['type'] == 'ether'
