# file: lib/ansible/module_utils/facts/network/generic_bsd.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import Mock

@pytest.fixture
def network_instance():
    module = Mock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_tunnel_line(network_instance):
    current_if = {}
    words = []
    ips = []

    network_instance.parse_tunnel_line(words, current_if, ips)

    assert current_if['type'] == 'tunnel'
