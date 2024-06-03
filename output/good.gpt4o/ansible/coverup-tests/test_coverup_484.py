# file lib/ansible/playbook/role_include.py:168-177
# lines [168, 170, 171, 172, 173, 174, 175, 177]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole, TaskInclude

class MockTaskInclude(TaskInclude):
    def __init__(self):
        self.statically_loaded = False
        self._from_files = {}
        self._parent_role = "parent_role"
        self._role_name = "role_name"
        self._role_path = "role_path"

@pytest.fixture
def mock_task_include():
    return MockTaskInclude()

def test_include_role_copy(mock_task_include):
    include_role = IncludeRole()
    include_role.statically_loaded = mock_task_include.statically_loaded
    include_role._from_files = mock_task_include._from_files
    include_role._parent_role = mock_task_include._parent_role
    include_role._role_name = mock_task_include._role_name
    include_role._role_path = mock_task_include._role_path

    new_include_role = include_role.copy()

    assert new_include_role.statically_loaded == include_role.statically_loaded
    assert new_include_role._from_files == include_role._from_files
    assert new_include_role._parent_role == include_role._parent_role
    assert new_include_role._role_name == include_role._role_name
    assert new_include_role._role_path == include_role._role_path
