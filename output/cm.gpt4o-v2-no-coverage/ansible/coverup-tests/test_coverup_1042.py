# file: lib/ansible/module_utils/facts/network/generic_bsd.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    module_mock = mocker.Mock()
    return GenericBsdIfconfigNetwork(module_mock)

def test_parse_tunnel_line(network_instance):
    words = ["tunnel"]
    current_if = {}
    ips = []

    network_instance.parse_tunnel_line(words, current_if, ips)

    assert current_if['type'] == 'tunnel'
