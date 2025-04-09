# file lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# lines []
# branches ['68->67']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.basic import AnsibleModule
import json
import sys

@pytest.fixture
def mock_ansible_module(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', json.dumps({'ANSIBLE_MODULE_ARGS': {}}).encode('utf-8'))
    return AnsibleModule(argument_spec={})

@pytest.fixture
def network(mock_ansible_module):
    return GenericBsdIfconfigNetwork(mock_ansible_module)

def test_detect_type_media(network):
    interfaces = {
        'eth0': {
            'media': 'Ethernet'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }

    expected_interfaces = {
        'eth0': {
            'media': 'Ethernet',
            'type': 'ether'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }

    result = network.detect_type_media(interfaces)
    assert result == expected_interfaces

def test_detect_type_media_no_media(network):
    interfaces = {
        'eth0': {
            'status': 'active'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }

    expected_interfaces = {
        'eth0': {
            'status': 'active'
        },
        'eth1': {
            'media': 'WiFi'
        }
    }

    result = network.detect_type_media(interfaces)
    assert result == expected_interfaces
