# file lib/ansible/plugins/action/copy.py:208-229
# lines [208, 214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229]
# branches ['214->215', '214->223', '215->216', '215->220', '223->224', '223->229', '224->225', '224->226', '226->227', '226->229']

import pytest
from ansible.plugins.action.copy import ActionModule
from ansible.playbook.play_context import PlayContext
from ansible.playbook.task import Task

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase._execute_module')
    play_context = PlayContext()
    task = Task()
    loader = mocker.MagicMock()
    return ActionModule(task, play_context, loader, mocker.MagicMock(), mocker.MagicMock(), mocker.MagicMock())

def test_ensure_invocation_no_log_set(action_module):
    action_module._play_context.no_log = True
    result = action_module._ensure_invocation({})
    assert result['invocation'] == "CENSORED: no_log is set"

def test_ensure_invocation_no_log_not_set(action_module):
    action_module._play_context.no_log = False
    action_module._task.args = {'content': 'some_content', 'other': 'value'}
    result = action_module._ensure_invocation({})
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert result['invocation']['other'] == 'value'

def test_ensure_invocation_already_set(action_module):
    action_module._play_context.no_log = False
    action_module._task.args = {'content': 'some_content', 'other': 'value'}
    result = action_module._ensure_invocation({'invocation': {'content': 'original_content', 'module_args': {'content': 'original_content'}}})
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert 'other' not in result['invocation']
