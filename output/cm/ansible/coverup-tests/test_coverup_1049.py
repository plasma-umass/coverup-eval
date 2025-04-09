# file lib/ansible/module_utils/facts/network/generic_bsd.py:271-272
# lines [271, 272]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    def __init__(self):
        pass

@pytest.fixture
def mock_module():
    return MockModule()

def test_parse_tunnel_line(mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    current_if = {}
    ips = []
    words = ['tunnel']

    network.parse_tunnel_line(words, current_if, ips)

    assert current_if['type'] == 'tunnel'
