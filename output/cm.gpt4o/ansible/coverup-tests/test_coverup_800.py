# file lib/ansible/playbook/role_include.py:68-70
# lines [68, 70]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_task_include(mocker):
    mocker.patch('ansible.playbook.role_include.TaskInclude', autospec=True)

def test_include_role_get_name_with_name(mock_task_include):
    role = IncludeRole()
    role.name = "test_name"
    role.action = "test_action"
    role._role_name = "test_role"
    assert role.get_name() == "test_name"

def test_include_role_get_name_without_name(mock_task_include):
    role = IncludeRole()
    role.name = None
    role.action = "test_action"
    role._role_name = "test_role"
    assert role.get_name() == "test_action : test_role"
