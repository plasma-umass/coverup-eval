# file: lib/ansible/plugins/action/include_vars.py:191-206
# asked: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

class MockActionModule(ActionModule):
    def __init__(self, ignore_files):
        self.ignore_files = ignore_files

@pytest.fixture
def action_module():
    return MockActionModule(ignore_files=[])

def test_ignore_file_match(action_module):
    action_module.ignore_files = ['txt']
    assert action_module._ignore_file('test.txt') is True

def test_ignore_file_no_match(action_module):
    action_module.ignore_files = ['txt']
    assert action_module._ignore_file('test.md') is False

def test_ignore_file_invalid_regex(action_module):
    action_module.ignore_files = ['[']
    with pytest.raises(AnsibleError, match='Invalid regular expression: \\['):
        action_module._ignore_file('test.txt')

def test_ignore_file_empty_ignore_list(action_module):
    action_module.ignore_files = []
    assert action_module._ignore_file('test.txt') is False
