# file: lib/ansible/playbook/role_include.py:168-177
# asked: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}
# gained: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def include_role_instance():
    return IncludeRole()

def test_include_role_copy(include_role_instance, mocker):
    # Mock the parent class's copy method
    mock_copy = mocker.patch.object(TaskInclude, 'copy', return_value=IncludeRole())

    # Set attributes to the instance
    include_role_instance.statically_loaded = True
    include_role_instance._from_files = {'key': 'value'}
    include_role_instance._parent_role = 'parent_role'
    include_role_instance._role_name = 'role_name'
    include_role_instance._role_path = 'role_path'

    # Call the copy method
    new_instance = include_role_instance.copy()

    # Assertions to verify the new instance has copied attributes
    assert new_instance.statically_loaded == include_role_instance.statically_loaded
    assert new_instance._from_files == include_role_instance._from_files
    assert new_instance._parent_role == include_role_instance._parent_role
    assert new_instance._role_name == include_role_instance._role_name
    assert new_instance._role_path == include_role_instance._role_path

    # Verify the parent class's copy method was called
    mock_copy.assert_called_once_with(exclude_parent=False, exclude_tasks=False)
