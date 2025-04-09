# file: lib/ansible/plugins/action/copy.py:208-229
# asked: {"lines": [214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [214, 223], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}
# gained: {"lines": [214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}

import pytest
from ansible.plugins.action.copy import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_result import TaskResult
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def action_module():
    play_context = PlayContext()
    task = Task()
    connection = None
    play = None
    loader = None
    variable_manager = None
    tqm = None
    return ActionModule(task, connection, play_context, loader, variable_manager, tqm)

def test_ensure_invocation_no_log(action_module, monkeypatch):
    result = {}
    action_module._play_context.no_log = True
    action_module._task.args = {'some_arg': 'some_value'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert result['invocation'] == "CENSORED: no_log is set"

def test_ensure_invocation_with_args(action_module, monkeypatch):
    result = {}
    action_module._play_context.no_log = False
    action_module._task.args = {'some_arg': 'some_value'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert result['invocation']['module_args'] == {'some_arg': 'some_value'}

def test_ensure_invocation_with_content(action_module, monkeypatch):
    result = {}
    action_module._play_context.no_log = False
    action_module._task.args = {'content': 'sensitive_data'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_ensure_invocation_with_no_content(action_module, monkeypatch):
    result = {}
    action_module._play_context.no_log = False
    action_module._task.args = {'some_arg': 'some_value'}
    
    result = action_module._ensure_invocation(result)
    
    assert 'invocation' in result
    assert 'content' not in result['invocation']
    assert 'content' not in result['invocation']['module_args']
