# file lib/ansible/module_utils/facts/network/generic_bsd.py:197-198
# lines [197, 198]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network_instance():
    return GenericBsdIfconfigNetwork(MockModule())

def test_parse_lladdr_line(network_instance):
    words = ['lladdr', '00:1a:2b:3c:4d:5e']
    current_if = {}
    ips = []

    network_instance.parse_lladdr_line(words, current_if, ips)

    assert 'lladdr' in current_if
    assert current_if['lladdr'] == '00:1a:2b:3c:4d:5e'
