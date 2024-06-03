# file lib/ansible/module_utils/facts/network/sunos.py:106-111
# lines [107, 108, 109, 110, 111]
# branches ['108->109', '108->111']

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork
from ansible.module_utils.basic import AnsibleModule
import json
import sys

@pytest.fixture
def sunos_network(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', json.dumps({'ANSIBLE_MODULE_ARGS': {}}).encode('utf-8'))
    module = AnsibleModule(argument_spec={})
    return SunOSNetwork(module)

def test_parse_ether_line(sunos_network):
    words = ['ether', '8:0:27:12:34:56']
    current_if = {}
    ips = []

    sunos_network.parse_ether_line(words, current_if, ips)

    assert 'macaddress' in current_if
    assert current_if['macaddress'] == '08:00:27:12:34:56'
