# file lib/ansible/module_utils/facts/network/generic_bsd.py:271-272
# lines [271, 272]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.basic import AnsibleModule
import json
import sys

@pytest.fixture
def mock_module(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', json.dumps({'ANSIBLE_MODULE_ARGS': {}}).encode('utf-8'))
    return AnsibleModule(argument_spec={})

@pytest.fixture
def network(mock_module):
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_tunnel_line(network):
    words = ['tunnel']
    current_if = {}
    ips = []

    network.parse_tunnel_line(words, current_if, ips)

    assert current_if['type'] == 'tunnel'
