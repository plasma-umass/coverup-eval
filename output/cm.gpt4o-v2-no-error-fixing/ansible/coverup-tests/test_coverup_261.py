# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}
# gained: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 35]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def action_module():
    loader = DataLoader()
    templar = Templar(loader=loader)
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=loader, templar=templar, shared_loader_obj=None)
    return action_module

def test_get_args_from_task_vars(action_module, mocker):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'},
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 2,
        'arg3': 'value3'
    }

    mock_template = mocker.patch.object(action_module._templar, 'template', side_effect=lambda x: x)
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {'arg1': 'value1', 'arg2': 2}
    mock_template.assert_called_once_with({'arg1': 'value1', 'arg2': 2})
