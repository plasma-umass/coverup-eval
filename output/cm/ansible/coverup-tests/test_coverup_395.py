# file lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# lines [66, 67, 68, 69, 70, 71]
# branches ['67->68', '67->71', '68->67', '68->69', '69->67', '69->70']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def generic_bsd_ifconfig_network():
    module_mock = MagicMock()
    return GenericBsdIfconfigNetwork(module=module_mock)

def test_detect_type_media_ether(generic_bsd_ifconfig_network):
    interfaces = {
        'em0': {
            'media': 'Ethernet autoselect (1000baseT <full-duplex>)'
        },
        'em1': {
            'media': 'Ethernet autoselect'
        },
        'lo0': {
            'media': 'Loopback'
        }
    }

    expected_interfaces = {
        'em0': {
            'media': 'Ethernet autoselect (1000baseT <full-duplex>)',
            'type': 'ether'
        },
        'em1': {
            'media': 'Ethernet autoselect',
            'type': 'ether'
        },
        'lo0': {
            'media': 'Loopback'
        }
    }

    result_interfaces = generic_bsd_ifconfig_network.detect_type_media(interfaces)
    assert result_interfaces == expected_interfaces

def test_detect_type_media_no_ether(generic_bsd_ifconfig_network):
    interfaces = {
        'lo0': {
            'media': 'Loopback'
        }
    }

    expected_interfaces = {
        'lo0': {
            'media': 'Loopback'
        }
    }

    result_interfaces = generic_bsd_ifconfig_network.detect_type_media(interfaces)
    assert result_interfaces == expected_interfaces
