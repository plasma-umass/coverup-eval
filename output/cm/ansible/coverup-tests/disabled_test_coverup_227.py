# file lib/ansible/playbook/task.py:106-120
# lines [106, 109, 110, 112, 113, 114, 115, 117, 118, 120]
# branches ['109->110', '109->112', '112->113', '112->114', '114->115', '114->117', '117->118', '117->120']

import pytest
from ansible.playbook.task import Task

# Mock Role class to return a predefined role name
class MockRole:
    def get_name(self, include_role_fqcn=True):
        return "test_role"

# Test function to cover all branches of Task.get_name
@pytest.fixture
def mock_role(mocker):
    mocker.patch('ansible.playbook.task.Role', new=MockRole)

def test_task_get_name(mock_role):
    # Test when role is not None and name is not None
    task_with_role_and_name = Task()
    task_with_role_and_name._role = MockRole()
    task_with_role_and_name.name = "task_name"
    task_with_role_and_name.action = "task_action"
    assert task_with_role_and_name.get_name() == "test_role : task_name"

    # Test when role is None and name is not None
    task_with_name_only = Task()
    task_with_name_only._role = None
    task_with_name_only.name = "task_name"
    task_with_name_only.action = "task_action"
    assert task_with_name_only.get_name() == "task_name"

    # Test when role is not None and name is None
    task_with_role_only = Task()
    task_with_role_only._role = MockRole()
    task_with_role_only.name = None
    task_with_role_only.action = "task_action"
    assert task_with_role_only.get_name() == "test_role : task_action"

    # Test when role is None and name is None
    task_with_no_name = Task()
    task_with_no_name._role = None
    task_with_no_name.name = None
    task_with_no_name.action = "task_action"
    assert task_with_no_name.get_name() == "task_action"
