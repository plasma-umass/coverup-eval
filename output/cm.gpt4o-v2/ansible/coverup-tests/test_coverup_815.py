# file: lib/ansible/module_utils/facts/network/generic_bsd.py:180-182
# asked: {"lines": [180, 181, 182], "branches": []}
# gained: {"lines": [180, 181, 182], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import Mock

@pytest.fixture
def network_instance():
    module = Mock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_ether_line(network_instance):
    words = ["ether", "00:11:22:33:44:55"]
    current_if = {}
    ips = []

    network_instance.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == "00:11:22:33:44:55"
    assert current_if['type'] == 'ether'
