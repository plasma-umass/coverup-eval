# file lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# lines [66, 67, 68, 69, 70, 71]
# branches ['67->68', '67->71', '68->67', '68->69', '69->67', '69->70']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_detect_type_media(network):
    interfaces = {
        'eth0': {
            'media': 'Ethernet 1000baseT'
        },
        'eth1': {
            'media': 'Wi-Fi 802.11'
        },
        'eth2': {
            'media': 'ethernet 100baseTX'
        },
        'eth3': {
            'media': 'Fiber 1000baseSX'
        }
    }

    expected_interfaces = {
        'eth0': {
            'media': 'Ethernet 1000baseT',
            'type': 'ether'
        },
        'eth1': {
            'media': 'Wi-Fi 802.11'
        },
        'eth2': {
            'media': 'ethernet 100baseTX',
            'type': 'ether'
        },
        'eth3': {
            'media': 'Fiber 1000baseSX'
        }
    }

    result = network.detect_type_media(interfaces)
    assert result == expected_interfaces
