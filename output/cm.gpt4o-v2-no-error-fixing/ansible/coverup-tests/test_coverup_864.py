# file: lib/ansible/plugins/action/copy.py:208-229
# asked: {"lines": [], "branches": [[214, 223]]}
# gained: {"lines": [], "branches": [[214, 223]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'content': 'some_content'}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_ensure_invocation_no_log(action_module):
    action_module._play_context.no_log = True
    result = {}
    result = action_module._ensure_invocation(result)
    assert result['invocation'] == "CENSORED: no_log is set"

def test_ensure_invocation_with_content(action_module):
    action_module._play_context.no_log = False
    result = {}
    result = action_module._ensure_invocation(result)
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_ensure_invocation_without_content(action_module):
    action_module._play_context.no_log = False
    action_module._task.args = {}
    result = {}
    result = action_module._ensure_invocation(result)
    assert 'content' not in result['invocation']
    assert 'content' not in result['invocation'].get('module_args', {})

def test_ensure_invocation_no_invocation_key(action_module):
    action_module._play_context.no_log = False
    action_module._task.args = {'other_key': 'other_value'}
    result = {}
    result = action_module._ensure_invocation(result)
    assert 'invocation' in result
    assert result['invocation']['module_args'] == {'other_key': 'other_value'}

def test_ensure_invocation_existing_invocation(action_module):
    action_module._play_context.no_log = False
    result = {'invocation': {'existing_key': 'existing_value'}}
    result = action_module._ensure_invocation(result)
    assert result['invocation']['existing_key'] == 'existing_value'
