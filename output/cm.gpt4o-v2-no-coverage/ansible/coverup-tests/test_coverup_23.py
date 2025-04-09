# file: lib/ansible/plugins/action/debug.py:33-80
# asked: {"lines": [33, 34, 35, 37, 38, 40, 41, 44, 46, 47, 48, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 64, 66, 68, 70, 73, 75, 76, 78, 80], "branches": [[34, 35], [34, 37], [37, 38], [37, 40], [46, 47], [46, 75], [47, 48], [47, 50], [50, 51], [50, 70], [53, 55], [53, 64], [55, 56], [55, 58], [61, 62], [61, 64], [64, 66], [64, 68]]}
# gained: {"lines": [33, 34, 35, 37, 38, 40, 41, 44, 46, 47, 48, 50, 51, 52, 53, 59, 60, 61, 62, 64, 68, 70, 73, 75, 76, 78, 80], "branches": [[34, 35], [37, 38], [37, 40], [46, 47], [46, 75], [47, 48], [47, 50], [50, 51], [50, 70], [53, 64], [61, 62], [64, 68]]}

import pytest
from ansible.plugins.action.debug import ActionModule
from ansible.errors import AnsibleUndefinedVariable, AnsibleActionFail
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    task.async_val = False
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_run_no_task_vars(action_module):
    result = action_module.run()
    assert result['failed'] is False

def test_run_msg_and_var_incompatible(action_module):
    action_module._task.args = {'msg': 'test', 'var': 'test'}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "'msg' and 'var' are incompatible options"

def test_run_msg(action_module):
    action_module._task.args = {'msg': 'test message'}
    action_module._display.verbosity = 0
    result = action_module.run()
    assert result['msg'] == 'test message'
    assert result['_ansible_verbose_always'] is True
    assert result['failed'] is False

def test_run_var(action_module):
    action_module._task.args = {'var': 'test_var'}
    action_module._templar.template = MagicMock(return_value='templated_var')
    action_module._display.verbosity = 0
    result = action_module.run()
    assert result['test_var'] == 'templated_var'
    assert result['_ansible_verbose_always'] is True
    assert result['failed'] is False

def test_run_var_undefined(action_module):
    action_module._task.args = {'var': 'test_var'}
    action_module._templar.template = MagicMock(side_effect=AnsibleUndefinedVariable)
    action_module._display.verbosity = 1
    result = action_module.run()
    assert result['test_var'] == "VARIABLE IS NOT DEFINED!: "
    assert result['_ansible_verbose_always'] is True
    assert result['failed'] is False

def test_run_default_msg(action_module):
    action_module._task.args = {}
    action_module._display.verbosity = 0
    result = action_module.run()
    assert result['msg'] == 'Hello world!'
    assert result['_ansible_verbose_always'] is True
    assert result['failed'] is False

def test_run_verbosity_not_met(action_module):
    action_module._task.args = {'verbosity': 2}
    action_module._display.verbosity = 0
    result = action_module.run()
    assert result['skipped_reason'] == "Verbosity threshold not met."
    assert result['skipped'] is True
    assert result['failed'] is False
