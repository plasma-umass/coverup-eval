# file: lib/ansible/plugins/action/copy.py:208-229
# asked: {"lines": [208, 214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [214, 223], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}
# gained: {"lines": [208, 214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [214, 223], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_ensure_invocation_no_log(action_module):
    result = {}
    action_module._play_context.no_log = True
    action_module._task.args = {'some_arg': 'some_value'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert result['invocation'] == "CENSORED: no_log is set"

def test_ensure_invocation_with_log(action_module):
    result = {}
    action_module._play_context.no_log = False
    action_module._task.args = {'some_arg': 'some_value'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert result['invocation']['some_arg'] == 'some_value'
    assert result['invocation']['module_args']['some_arg'] == 'some_value'

def test_ensure_invocation_with_content(action_module):
    result = {'invocation': {'content': 'secret', 'module_args': {'content': 'secret'}}}
    action_module._play_context.no_log = False
    action_module._task.args = {'some_arg': 'some_value', 'content': 'secret'}
    
    result = action_module._ensure_invocation(result)
    
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
