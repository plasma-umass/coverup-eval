# file lib/ansible/plugins/action/copy.py:208-229
# lines [214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229]
# branches ['214->215', '214->223', '215->216', '215->220', '223->224', '223->229', '224->225', '224->226', '226->227', '226->229']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'content': 'some_content'}
    play_context = MagicMock()
    play_context.no_log = False
    connection = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_ensure_invocation_no_log(action_module):
    result = {}
    action_module._play_context.no_log = True
    result = action_module._ensure_invocation(result)
    assert result['invocation'] == "CENSORED: no_log is set"

def test_ensure_invocation_with_content(action_module):
    result = {}
    action_module._play_context.no_log = False
    result = action_module._ensure_invocation(result)
    assert 'invocation' in result
    assert 'content' in result['invocation']
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_ensure_invocation_without_content(action_module):
    result = {}
    action_module._task.args = {'other_arg': 'some_value'}
    result = action_module._ensure_invocation(result)
    assert 'invocation' in result
    assert 'content' not in result['invocation']
    assert 'content' not in result['invocation']['module_args']
