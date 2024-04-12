# file lib/ansible/playbook/task.py:136-139
# lines [136, 137, 138, 139]
# branches []

import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_block(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_role(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock()

def test_task_load_with_action(mock_block, mock_role, mock_variable_manager, mock_loader):
    data = {
        'name': 'Test Task',
        'action': 'dummy_action',
        'collections': ['ansible.builtin']
    }
    task = Task.load(data, block=mock_block, role=mock_role, variable_manager=mock_variable_manager, loader=mock_loader)
    assert isinstance(task, Task)
    assert task.name == 'Test Task'

def test_task_load_without_action_raises_error(mock_block, mock_role, mock_variable_manager, mock_loader):
    data = {'name': 'Test Task'}
    with pytest.raises(AnsibleParserError):
        Task.load(data, block=mock_block, role=mock_role, variable_manager=mock_variable_manager, loader=mock_loader)
