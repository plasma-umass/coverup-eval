# file: lib/ansible/playbook/task.py:256-264
# asked: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}
# gained: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}

import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError
from ansible.playbook.loop_control import LoopControl

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def task():
    class MockTask(Task):
        def __init__(self):
            self._variable_manager = MockVariableManager()
            self._loader = MockLoader()
    return MockTask()

def test_load_loop_control_with_dict(task, mocker):
    mocker.patch.object(LoopControl, 'load', return_value='mocked_loop_control')
    ds = {'key': 'value'}
    result = task._load_loop_control('attr', ds)
    assert result == 'mocked_loop_control'
    LoopControl.load.assert_called_once_with(data=ds, variable_manager=task._variable_manager, loader=task._loader)

def test_load_loop_control_with_non_dict(task):
    ds = ['not', 'a', 'dict']
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control('attr', ds)
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)
