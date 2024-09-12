# file: lib/ansible/playbook/task.py:256-264
# asked: {"lines": [256, 257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}
# gained: {"lines": [256, 257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.task import Task
from ansible.playbook.loop_control import LoopControl

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def task():
    task = Task()
    task._variable_manager = MockVariableManager()
    task._loader = MockLoader()
    return task

def test_load_loop_control_with_invalid_data(task):
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control('loop_control', 'not_a_dict')
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)

def test_load_loop_control_with_valid_data(task, mocker):
    mocker.patch.object(LoopControl, 'load', return_value='mocked_loop_control')
    ds = {'key': 'value'}
    result = task._load_loop_control('loop_control', ds)
    assert result == 'mocked_loop_control'
    LoopControl.load.assert_called_once_with(data=ds, variable_manager=task._variable_manager, loader=task._loader)
