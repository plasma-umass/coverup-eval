# file lib/ansible/plugins/action/include_vars.py:191-206
# lines [199, 200, 201, 202, 203, 204, 205, 206]
# branches ['199->200', '199->206', '201->199', '201->202']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    class MockActionModule(ActionModule):
        def __init__(self):
            self.ignore_files = []

    return MockActionModule()

def test_ignore_file_with_valid_regex(action_module):
    action_module.ignore_files = ['\\.txt', '\\.log']
    assert action_module._ignore_file('test.txt') is True
    assert action_module._ignore_file('test.log') is True
    assert action_module._ignore_file('test.py') is False

def test_ignore_file_with_invalid_regex(action_module):
    action_module.ignore_files = ['[invalid']
    with pytest.raises(AnsibleError, match='Invalid regular expression: \[invalid'):
        action_module._ignore_file('test.txt')
