# file lib/ansible/playbook/task.py:378-392
# lines [379, 381, 382, 383, 385, 386, 387, 389, 390, 392]
# branches ['382->383', '382->385', '386->387', '386->389']

import pytest
from ansible.playbook.task import Task

@pytest.fixture
def mock_task(mocker):
    task = Task()
    task._parent = mocker.MagicMock()
    task._role = mocker.MagicMock()
    task.implicit = False
    task.resolved_action = None
    return task

def test_task_copy_includes_parent_and_role(mock_task):
    # Copy the task without excluding parent and tasks
    new_task = mock_task.copy(exclude_parent=False, exclude_tasks=False)

    # Assertions to ensure the lines 379-392 are executed
    assert new_task._parent is not None
    assert new_task._role is not None
    assert new_task.implicit == mock_task.implicit
    assert new_task.resolved_action == mock_task.resolved_action

    # Clean up
    mock_task._parent = None
    mock_task._role = None
