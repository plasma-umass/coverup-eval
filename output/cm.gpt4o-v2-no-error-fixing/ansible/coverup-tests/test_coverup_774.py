# file: lib/ansible/plugins/action/include_vars.py:191-206
# asked: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

class MockActionModule(ActionModule):
    def __init__(self, ignore_files):
        self.ignore_files = ignore_files

def test_ignore_file_matches(monkeypatch):
    action_module = MockActionModule(ignore_files=['.txt', '.log'])
    assert action_module._ignore_file('test.txt') is True
    assert action_module._ignore_file('test.log') is True

def test_ignore_file_no_match(monkeypatch):
    action_module = MockActionModule(ignore_files=['.txt', '.log'])
    assert action_module._ignore_file('test.py') is False

def test_ignore_file_invalid_regex(monkeypatch):
    action_module = MockActionModule(ignore_files=['[invalid'])
    with pytest.raises(AnsibleError) as excinfo:
        action_module._ignore_file('test.txt')
    assert 'Invalid regular expression' in str(excinfo.value)
