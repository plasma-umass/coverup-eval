# file: lib/ansible/plugins/action/copy.py:208-229
# asked: {"lines": [214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [214, 223], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}
# gained: {"lines": [214, 215, 216, 220, 221, 223, 224, 225, 226, 227, 229], "branches": [[214, 215], [214, 223], [215, 216], [215, 220], [223, 224], [223, 229], [224, 225], [224, 226], [226, 227], [226, 229]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'content': 'some_content', 'other_arg': 'value'}
    play_context = MagicMock()
    connection = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, play_context, connection, loader, templar, shared_loader_obj)

def test_ensure_invocation_no_log(action_module):
    action_module._play_context.no_log = True
    result = {}
    result = action_module._ensure_invocation(result)
    assert result['invocation'] == 'CENSORED: no_log is set'

def test_ensure_invocation_with_args(action_module):
    action_module._play_context.no_log = False
    result = {}
    result = action_module._ensure_invocation(result)
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'
    assert result['invocation']['other_arg'] == 'value'
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert result['invocation']['module_args']['other_arg'] == 'value'

def test_ensure_invocation_censor_content(action_module):
    action_module._play_context.no_log = False
    result = {'invocation': {'content': 'some_content'}}
    result = action_module._ensure_invocation(result)
    assert result['invocation']['content'] == 'CENSORED: content is a no_log parameter'

def test_ensure_invocation_censor_module_args_content(action_module):
    action_module._play_context.no_log = False
    result = {'invocation': {'module_args': {'content': 'some_content'}}}
    result = action_module._ensure_invocation(result)
    assert result['invocation']['module_args']['content'] == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
