# file: lib/ansible/module_utils/facts/network/sunos.py:106-111
# asked: {"lines": [106, 107, 108, 109, 110, 111], "branches": [[108, 109], [108, 111]]}
# gained: {"lines": [106, 107, 108, 109, 110, 111], "branches": [[108, 109], [108, 111]]}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    pass

@pytest.fixture
def sunos_network():
    module = MockModule()
    return SunOSNetwork(module)

def test_parse_ether_line(sunos_network):
    words = ['ether', '8:0:27:ce:76:1']
    current_if = {}
    ips = []

    sunos_network.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == '08:00:27:ce:76:01'
