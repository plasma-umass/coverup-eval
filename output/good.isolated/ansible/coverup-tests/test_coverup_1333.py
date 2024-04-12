# file lib/ansible/module_utils/facts/network/aix.py:135-140
# lines [136, 137, 138, 139, 140]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def aix_network(mocker):
    mocker.patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork.__init__', return_value=None)
    mocker.patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork.get_options', return_value=['UP', 'BROADCAST', 'NOTRAILERS', 'SIMPLEX', 'MULTICAST'])
    return AIXNetwork()

def test_parse_interface_line(aix_network):
    words = ['en0:', 'UP,BROADCAST,NOTRAILERS,SIMPLEX,MULTICAST']
    expected_current_if = {
        'device': 'en0',
        'ipv4': [],
        'ipv6': [],
        'type': 'unknown',
        'flags': ['UP', 'BROADCAST', 'NOTRAILERS', 'SIMPLEX', 'MULTICAST'],
        'macaddress': 'unknown'
    }
    current_if = aix_network.parse_interface_line(words)
    assert current_if == expected_current_if
