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
            'media': 'Ethernet'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }
    expected = {
        'eth0': {
            'media': 'Ethernet',
            'type': 'ether'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected

def test_detect_type_media_without_ether(network_instance):
    interfaces = {
        'eth0': {
            'media': 'WiFi'
        },
        'eth1': {
            'media': 'Bluetooth'
        }
    }
    expected = {
        'eth0': {
            'media': 'WiFi'
        },
        'eth1': {
            'media': 'Bluetooth'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected

def test_detect_type_media_no_media_key(network_instance):
    interfaces = {
        'eth0': {},
        'eth1': {
            'media': 'WiFi'
        }
    }
    expected = {
        'eth0': {},
        'eth1': {
            'media': 'WiFi'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result == expected
