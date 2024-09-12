# file: lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# asked: {"lines": [66, 67, 68, 69, 70, 71], "branches": [[67, 68], [67, 71], [68, 67], [68, 69], [69, 67], [69, 70]]}
# gained: {"lines": [66, 67, 68, 69, 70, 71], "branches": [[67, 68], [67, 71], [68, 67], [68, 69], [69, 67], [69, 70]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import MagicMock

@pytest.fixture
def network_instance():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module)

def test_detect_type_media_with_ether(network_instance):
    interfaces = {
        'eth0': {
            'media': 'Ethernet 1000baseT'
        },
        'eth1': {
            'media': 'Wi-Fi 802.11ac'
        }
    }
    expected_result = {
        'eth0': {
            'media': 'Ethernet 1000baseT',
            'type': 'ether'
        },
        'eth1': {
            'media': 'Wi-Fi 802.11ac'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected_result

def test_detect_type_media_without_ether(network_instance):
    interfaces = {
        'eth0': {
            'media': 'Wi-Fi 802.11ac'
        },
        'eth1': {
            'media': 'Bluetooth'
        }
    }
    expected_result = {
        'eth0': {
            'media': 'Wi-Fi 802.11ac'
        },
        'eth1': {
            'media': 'Bluetooth'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected_result

def test_detect_type_media_no_media_key(network_instance):
    interfaces = {
        'eth0': {
            'status': 'active'
        },
        'eth1': {
            'status': 'inactive'
        }
    }
    expected_result = {
        'eth0': {
            'status': 'active'
        },
        'eth1': {
            'status': 'inactive'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected_result
