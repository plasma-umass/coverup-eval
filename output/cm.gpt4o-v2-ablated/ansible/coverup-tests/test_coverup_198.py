# file: lib/ansible/playbook/role_include.py:168-177
# asked: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}
# gained: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.task_include import TaskInclude

class MockTaskInclude(TaskInclude):
    def __init__(self):
        self.statically_loaded = False
        self._from_files = {}
        self._parent_role = "parent_role"
        self._role_name = "role_name"
        self._role_path = "role_path"

    def copy(self, exclude_parent=False, exclude_tasks=False):
        return super(MockTaskInclude, self).copy(exclude_parent=exclude_parent, exclude_tasks=exclude_tasks)

@pytest.fixture
def include_role():
    return IncludeRole()

def test_copy_method(include_role, mocker):
    mocker.patch.object(TaskInclude, 'copy', return_value=MockTaskInclude())
    
    include_role.statically_loaded = True
    include_role._from_files = {'file1': 'content1'}
    include_role._parent_role = 'test_parent_role'
    include_role._role_name = 'test_role_name'
    include_role._role_path = 'test_role_path'
    
    new_role = include_role.copy(exclude_parent=True, exclude_tasks=True)
    
    assert new_role.statically_loaded == include_role.statically_loaded
    assert new_role._from_files == include_role._from_files
    assert new_role._parent_role == include_role._parent_role
    assert new_role._role_name == include_role._role_name
    assert new_role._role_path == include_role._role_path
