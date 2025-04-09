# file: lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# asked: {"lines": [66, 67, 68, 69, 70, 71], "branches": [[67, 68], [67, 71], [68, 67], [68, 69], [69, 67], [69, 70]]}
# gained: {"lines": [66, 67, 68, 69, 70, 71], "branches": [[67, 68], [67, 71], [68, 67], [68, 69], [69, 67], [69, 70]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance():
    return GenericBsdIfconfigNetwork(module=None)

def test_detect_type_media_with_ether(network_instance):
    interfaces = {
        'eth0': {
            'media': 'Ethernet'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert result['eth0']['type'] == 'ether'

def test_detect_type_media_without_ether(network_instance):
    interfaces = {
        'eth0': {
            'media': 'WiFi'
        }
    }
    result = network_instance.detect_type_media(interfaces)
    assert 'type' not in result['eth0']

def test_detect_type_media_no_media_key(network_instance):
    interfaces = {
        'eth0': {}
    }
    result = network_instance.detect_type_media(interfaces)
    assert 'type' not in result['eth0']
