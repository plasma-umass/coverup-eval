# file: lib/ansible/playbook/role_include.py:168-177
# asked: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}
# gained: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.task_include import TaskInclude

class MockTaskInclude(TaskInclude):
    def __init__(self, block=None, role=None, task_include=None):
        super(MockTaskInclude, self).__init__(block=block, role=role, task_include=task_include)
        self.statically_loaded = True

def test_include_role_copy(monkeypatch):
    # Arrange
    original_role = MockTaskInclude()
    include_role = IncludeRole(role=original_role)
    include_role._from_files = {'file1': 'content1'}
    include_role._parent_role = 'parent_role'
    include_role._role_name = 'role_name'
    include_role._role_path = 'role_path'

    # Act
    copied_role = include_role.copy()

    # Assert
    assert copied_role.statically_loaded == include_role.statically_loaded
    assert copied_role._from_files == include_role._from_files
    assert copied_role._parent_role == include_role._parent_role
    assert copied_role._role_name == include_role._role_name
    assert copied_role._role_path == include_role._role_path
    assert copied_role is not include_role
