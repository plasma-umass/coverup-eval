# file: lib/ansible/module_utils/facts/network/generic_bsd.py:271-272
# asked: {"lines": [272], "branches": []}
# gained: {"lines": [272], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_parse_tunnel_line(network):
    words = ['tunnel']
    current_if = {}
    ips = []

    network.parse_tunnel_line(words, current_if, ips)

    assert current_if['type'] == 'tunnel'
