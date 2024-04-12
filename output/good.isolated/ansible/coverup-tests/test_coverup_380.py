# file lib/ansible/playbook/task.py:491-497
# lines [491, 492, 493, 494, 495, 496, 497]
# branches ['493->494', '493->497', '494->495', '494->496']

import pytest
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

# Mock class to simulate a parent that is not a TaskInclude
class MockParentTask(Task):
    def get_first_parent_include(self):
        return None

@pytest.fixture
def mock_task_include(mocker):
    mock_task_include = mocker.MagicMock(spec=TaskInclude)
    return mock_task_include

@pytest.fixture
def mock_parent_task(mocker):
    mock_parent_task = mocker.MagicMock(spec=MockParentTask)
    return mock_parent_task

def test_get_first_parent_include_with_task_include_parent(mock_task_include):
    task = Task()
    task._parent = mock_task_include
    assert task.get_first_parent_include() is mock_task_include

def test_get_first_parent_include_with_non_task_include_parent(mock_parent_task, mock_task_include):
    task = Task()
    task._parent = mock_parent_task
    mock_parent_task.get_first_parent_include.return_value = mock_task_include
    assert task.get_first_parent_include() is mock_task_include

def test_get_first_parent_include_with_no_parent():
    task = Task()
    task._parent = None
    assert task.get_first_parent_include() is None
