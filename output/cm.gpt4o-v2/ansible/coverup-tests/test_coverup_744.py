# file: lib/ansible/plugins/action/include_vars.py:208-216
# asked: {"lines": [208, 215, 216], "branches": []}
# gained: {"lines": [208, 215, 216], "branches": []}

import pytest
from os import path
from ansible.plugins.action.include_vars import ActionModule

class MockActionModule(ActionModule):
    def __init__(self):
        self.valid_extensions = ['yaml', 'yml', 'json']

@pytest.fixture
def action_module():
    return MockActionModule()

def test_is_valid_file_ext_valid_extension(action_module):
    assert action_module._is_valid_file_ext('test.yaml') is True
    assert action_module._is_valid_file_ext('test.yml') is True
    assert action_module._is_valid_file_ext('test.json') is True

def test_is_valid_file_ext_invalid_extension(action_module):
    assert action_module._is_valid_file_ext('test.txt') is False
    assert action_module._is_valid_file_ext('test') is False

def test_is_valid_file_ext_no_extension(action_module):
    assert action_module._is_valid_file_ext('testfile') is False

def test_is_valid_file_ext_hidden_file(action_module):
    assert action_module._is_valid_file_ext('.testfile') is False

def test_is_valid_file_ext_multiple_dots(action_module):
    assert action_module._is_valid_file_ext('test.file.yaml') is True
    assert action_module._is_valid_file_ext('test.file.txt') is False
