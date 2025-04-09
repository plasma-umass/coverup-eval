# file: lib/ansible/module_utils/facts/network/generic_bsd.py:176-178
# asked: {"lines": [176, 178], "branches": []}
# gained: {"lines": [176, 178], "branches": []}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.basic import AnsibleModule
import json

@pytest.fixture
def network_instance(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', json.dumps({'ANSIBLE_MODULE_ARGS': {}}).encode('utf-8'))
    module = AnsibleModule(argument_spec={})
    return GenericBsdIfconfigNetwork(module)

def test_parse_nd6_line_with_options(network_instance, mocker):
    words = ['nd6', 'option1']
    current_if = {}
    ips = []

    mocker.patch.object(network_instance, 'get_options', return_value='mocked_option')

    network_instance.parse_nd6_line(words, current_if, ips)

    assert 'options' in current_if
    assert current_if['options'] == 'mocked_option'
