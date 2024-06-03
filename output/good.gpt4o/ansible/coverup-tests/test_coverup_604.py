# file lib/ansible/module_utils/facts/network/aix.py:135-140
# lines [135, 136, 137, 138, 139, 140]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork
from ansible.module_utils.basic import AnsibleModule
import json
import sys

@pytest.fixture
def mock_ansible_module(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', json.dumps({'ANSIBLE_MODULE_ARGS': {}}).encode('utf-8'))
    return AnsibleModule(argument_spec={})

def test_parse_interface_line(mock_ansible_module):
    network = AIXNetwork(mock_ansible_module)
    words = ['en0:', 'flags=4b<UP,BROADCAST,RUNNING,MULTICAST>']
    
    result = network.parse_interface_line(words)
    
    assert result['device'] == 'en0'
    assert result['ipv4'] == []
    assert result['ipv6'] == []
    assert result['type'] == 'unknown'
    assert result['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST']
    assert result['macaddress'] == 'unknown'
