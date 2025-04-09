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

def test_load_loop_control_with_valid_dict(task):
    ds = {'loop_var': 'item', 'pause': 1.0}
    result = task._load_loop_control('attr', ds)
    assert isinstance(result, LoopControl)

def test_load_loop_control_with_invalid_dict(task):
    ds = {'key': 'value'}
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control('attr', ds)
    assert "'key' is not a valid attribute for a LoopControl" in str(excinfo.value)

def test_load_loop_control_with_non_dict(task):
    ds = ['not', 'a', 'dict']
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control('attr', ds)
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)
