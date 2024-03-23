# file lib/ansible/playbook/task.py:370-376
# lines [371, 372, 373, 374, 375, 376]
# branches ['372->373', '372->374', '374->375', '374->376']

import pytest
from ansible.playbook.task import Task

# Mocking the necessary parts of the ansible module
class MockParent:
    def get_include_params(self):
        return {'parent_param': 'parent_value'}

@pytest.fixture
def mock_task(mocker):
    task = Task()
    task._parent = MockParent()
    task.action = 'mock_include_action'
    task.vars = {'task_var': 'task_value'}
    # Mocking the C._ACTION_ALL_INCLUDES directly as the import failed
    mocker.patch('ansible.playbook.task.C._ACTION_ALL_INCLUDES', new=['mock_include_action'])
    return task

def test_get_include_params(mock_task):
    # Test to cover lines 371-376
    all_vars = mock_task.get_include_params()
    assert all_vars == {'parent_param': 'parent_value', 'task_var': 'task_value'}
