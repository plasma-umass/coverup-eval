# file lib/ansible/playbook/task.py:256-264
# lines [256, 257, 258, 259, 261, 264]
# branches ['257->258', '257->264']

import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError
from unittest.mock import Mock

def test_load_loop_control_invalid_type():
    task = Task()
    invalid_ds = "not_a_dict"
    
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control(attr=None, ds=invalid_ds)
    
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)

def test_load_loop_control_valid_type(mocker):
    task = Task()
    valid_ds = {"key": "value"}
    
    mocker.patch.object(task, '_variable_manager', Mock())
    mocker.patch.object(task, '_loader', Mock())
    mock_loop_control = mocker.patch('ansible.playbook.task.LoopControl.load', return_value="mocked_loop_control")
    
    result = task._load_loop_control(attr=None, ds=valid_ds)
    
    mock_loop_control.assert_called_once_with(data=valid_ds, variable_manager=task._variable_manager, loader=task._loader)
    assert result == "mocked_loop_control"
