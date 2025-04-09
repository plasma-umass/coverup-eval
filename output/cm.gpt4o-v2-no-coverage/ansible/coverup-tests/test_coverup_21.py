# file: lib/ansible/plugins/action/set_stats.py:33-77
# asked: {"lines": [33, 34, 35, 37, 38, 40, 42, 43, 45, 46, 48, 49, 50, 51, 54, 55, 56, 57, 58, 60, 62, 64, 66, 67, 68, 69, 70, 72, 74, 75, 77], "branches": [[34, 35], [34, 37], [42, 43], [42, 74], [45, 46], [45, 48], [48, 49], [48, 54], [54, 55], [54, 62], [56, 54], [56, 57], [57, 58], [57, 60], [62, 64], [62, 74], [66, 67], [66, 72]]}
# gained: {"lines": [33, 34, 35, 37, 38, 40, 42, 43, 45, 46, 48, 49, 50, 51, 54, 55, 56, 57, 58, 62, 64, 66, 67, 68, 69, 70, 72, 74, 75, 77], "branches": [[34, 35], [42, 43], [42, 74], [45, 46], [45, 48], [48, 49], [48, 54], [54, 55], [54, 62], [56, 54], [56, 57], [57, 58], [62, 64], [62, 74], [66, 67], [66, 72]]}

import pytest
from ansible.plugins.action.set_stats import ActionModule
from ansible.plugins.action import ActionBase
from unittest.mock import MagicMock, patch

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    task.async_val = False
    templar = MagicMock()
    play_context = MagicMock()
    play_context.check_mode = False
    connection = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task, None, None, templar, connection, play_context)

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_no_task_vars(mock_run, action_module):
    result = action_module.run()
    assert result['changed'] == False
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_non_dict_data(mock_run, action_module):
    action_module._task.args = {'data': 'non_dict'}
    action_module._templar.template.return_value = 'non_dict'
    result = action_module.run()
    assert result['failed'] == True
    assert result['msg'] == "The 'data' option needs to be a dictionary/hash"

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_invalid_variable_name(mock_run, action_module):
    action_module._task.args = {'data': {'1invalid': 'value'}}
    action_module._templar.template.side_effect = lambda x, **kwargs: x
    result = action_module.run()
    assert result['failed'] == True
    assert result['msg'] == "The variable name '1invalid' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_valid_data(mock_run, action_module):
    action_module._task.args = {'data': {'valid_name': 'value'}}
    action_module._templar.template.side_effect = lambda x, **kwargs: x
    result = action_module.run()
    assert result['changed'] == False
    assert result['ansible_stats'] == {'data': {'valid_name': 'value'}, 'per_host': False, 'aggregate': True}

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_boolean_options(mock_run, action_module):
    action_module._task.args = {'data': {}, 'per_host': 'yes', 'aggregate': 'no'}
    action_module._templar.template.side_effect = lambda x, **kwargs: x
    result = action_module.run()
    assert result['changed'] == False
    assert result['ansible_stats'] == {'data': {}, 'per_host': True, 'aggregate': False}
