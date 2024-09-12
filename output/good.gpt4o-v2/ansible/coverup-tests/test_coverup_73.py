# file: lib/ansible/plugins/action/set_fact.py:30-68
# asked: {"lines": [30, 32, 34, 35, 36, 38, 39, 41, 42, 44, 45, 46, 48, 49, 50, 54, 55, 56, 58, 60, 62, 63, 66, 68], "branches": [[35, 36], [35, 38], [44, 45], [44, 58], [45, 46], [45, 60], [48, 49], [48, 54], [54, 55], [54, 56], [60, 62], [60, 66]]}
# gained: {"lines": [30, 32, 34, 35, 36, 38, 39, 41, 42, 44, 45, 46, 48, 49, 50, 54, 55, 56, 58, 60, 62, 63, 68], "branches": [[35, 36], [44, 45], [44, 58], [45, 46], [45, 60], [48, 49], [48, 54], [54, 55], [54, 56], [60, 62]]}

import pytest
from ansible.plugins.action.set_fact import ActionModule
from ansible.errors import AnsibleActionFail
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.utils.vars import isidentifier
import ansible.constants as C
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    task = MagicMock()
    task.async_val = False
    task.args = {}
    play_context = MagicMock()
    play_context.check_mode = False
    connection = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task=task, connection=connection, play_context=play_context, loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

def test_run_no_task_vars(action_module):
    action_module._task.args = {'key': 'value'}
    action_module._templar.template = lambda x: x
    result = action_module.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts'] == {'key': 'value'}
    assert result['_ansible_facts_cacheable'] is False

def test_run_invalid_variable_name(action_module):
    action_module._task.args = {'1invalid': 'value'}
    action_module._templar.template = lambda x: x
    with pytest.raises(AnsibleActionFail, match="The variable name '1invalid' is not valid."):
        action_module.run()

def test_run_no_key_value_pairs(action_module):
    action_module._task.args = {}
    with pytest.raises(AnsibleActionFail, match="No key/value pairs provided, at least one is required for this action to succeed"):
        action_module.run()

def test_run_boolean_conversion(action_module):
    action_module._task.args = {'key': 'yes'}
    action_module._templar.template = lambda x: x
    result = action_module.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts'] == {'key': True}

def test_run_cacheable(action_module):
    action_module._task.args = {'key': 'value', 'cacheable': True}
    action_module._templar.template = lambda x: x
    result = action_module.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts'] == {'key': 'value'}
    assert result['_ansible_facts_cacheable'] is True

def test_run_no_facts_created(action_module):
    action_module._task.args = {}
    with pytest.raises(AnsibleActionFail, match="No key/value pairs provided, at least one is required for this action to succeed"):
        action_module.run()
