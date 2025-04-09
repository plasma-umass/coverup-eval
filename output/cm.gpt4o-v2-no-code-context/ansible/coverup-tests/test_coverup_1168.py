# file: lib/ansible/plugins/action/include_vars.py:191-206
# asked: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 205, 206], "branches": [[199, 200], [199, 206], [201, 199], [201, 202]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module.ignore_files = []
    return module

def test_ignore_file_match(action_module, monkeypatch):
    monkeypatch.setattr(action_module, 'ignore_files', ['ignore_this'])
    assert action_module._ignore_file('ignore_this') is True

def test_ignore_file_no_match(action_module, monkeypatch):
    monkeypatch.setattr(action_module, 'ignore_files', ['ignore_this'])
    assert action_module._ignore_file('do_not_ignore_this.txt') is False

def test_ignore_file_partial_match(action_module, monkeypatch):
    monkeypatch.setattr(action_module, 'ignore_files', ['ignore_this'])
    assert action_module._ignore_file('ignore_this_file.txt') is False

def test_ignore_file_invalid_regex(action_module, monkeypatch):
    monkeypatch.setattr(action_module, 'ignore_files', ['[invalid'])
    with pytest.raises(AnsibleError, match=r'Invalid regular expression: \[invalid'):
        action_module._ignore_file('some_file')
