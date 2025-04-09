# file: lib/ansible/playbook/task.py:256-264
# asked: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}
# gained: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}

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
    return Task()

def test_load_loop_control_with_invalid_ds(task):
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control(attr=None, ds="not_a_dict")
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)

def test_load_loop_control_with_valid_ds(task, mocker):
    mock_variable_manager = MockVariableManager()
    mock_loader = MockLoader()
    mocker.patch.object(task, '_variable_manager', mock_variable_manager)
    mocker.patch.object(task, '_loader', mock_loader)
    mocker.patch.object(LoopControl, 'load', return_value="mocked_loop_control")

    ds = {"key": "value"}
    result = task._load_loop_control(attr=None, ds=ds)
    assert result == "mocked_loop_control"
    LoopControl.load.assert_called_once_with(data=ds, variable_manager=mock_variable_manager, loader=mock_loader)
