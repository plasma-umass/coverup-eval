# file: lib/ansible/plugins/action/include_vars.py:208-216
# asked: {"lines": [208, 215, 216], "branches": []}
# gained: {"lines": [208, 215, 216], "branches": []}

import pytest
from os import path
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    class MockActionModule(ActionModule):
        def __init__(self):
            self.valid_extensions = ['yaml', 'yml', 'json']
    return MockActionModule()

def test_is_valid_file_ext_valid(action_module):
    assert action_module._is_valid_file_ext('test.yaml') is True
    assert action_module._is_valid_file_ext('test.yml') is True
    assert action_module._is_valid_file_ext('test.json') is True

def test_is_valid_file_ext_invalid(action_module):
    assert action_module._is_valid_file_ext('test.txt') is False
    assert action_module._is_valid_file_ext('test') is False
    assert action_module._is_valid_file_ext('test.') is False
    assert action_module._is_valid_file_ext('test.yaml.txt') is False
