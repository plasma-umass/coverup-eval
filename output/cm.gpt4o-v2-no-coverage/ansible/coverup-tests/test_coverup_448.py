# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}
# gained: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 35]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._templar = MagicMock(spec=Templar)
    return action

def test_get_args_from_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'},
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 2,
        'arg3': 'value3'
    }
    
    action_module._templar.template.return_value = {
        'arg1': 'value1',
        'arg2': 2
    }
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {
        'arg1': 'value1',
        'arg2': 2
    }
    action_module._templar.template.assert_called_once_with({
        'arg1': 'value1',
        'arg2': 2
    })
