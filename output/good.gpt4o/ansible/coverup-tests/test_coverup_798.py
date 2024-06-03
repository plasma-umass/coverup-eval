# file lib/ansible/module_utils/facts/network/generic_bsd.py:180-182
# lines [180, 181, 182]
# branches []

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
def network_instance(mock_ansible_module):
    return GenericBsdIfconfigNetwork(mock_ansible_module)

def test_parse_ether_line(network_instance):
    words = ['ether', '00:1a:2b:3c:4d:5e']
    current_if = {}
    ips = []

    network_instance.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == '00:1a:2b:3c:4d:5e'
    assert current_if['type'] == 'ether'
