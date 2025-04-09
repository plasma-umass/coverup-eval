# file: lib/ansible/module_utils/facts/network/generic_bsd.py:194-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

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

def test_parse_status_line(network_instance):
    words = ["status:", "active"]
    current_if = {}
    ips = []

    network_instance.parse_status_line(words, current_if, ips)

    assert current_if['status'] == "active"

def test_parse_status_line_inactive(network_instance):
    words = ["status:", "inactive"]
    current_if = {}
    ips = []

    network_instance.parse_status_line(words, current_if, ips)

    assert current_if['status'] == "inactive"
