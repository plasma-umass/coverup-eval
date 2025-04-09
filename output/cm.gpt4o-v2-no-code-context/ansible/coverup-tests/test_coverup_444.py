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
        new_me = MockTaskInclude()
        new_me.statically_loaded = self.statically_loaded
        new_me._from_files = self._from_files.copy()
        new_me._parent_role = self._parent_role
        new_me._role_name = self._role_name
        new_me._role_path = self._role_path
        return new_me

@pytest.fixture
def include_role():
    return IncludeRole()

def test_include_role_copy(mocker):
    mock_task_include = MockTaskInclude()
    mocker.patch('ansible.playbook.role_include.TaskInclude', return_value=mock_task_include)
    
    include_role_instance = IncludeRole()
    include_role_instance.statically_loaded = False
    include_role_instance._from_files = {}
    include_role_instance._parent_role = "parent_role"
    include_role_instance._role_name = "role_name"
    include_role_instance._role_path = "role_path"
    
    new_instance = include_role_instance.copy()

    assert new_instance.statically_loaded == include_role_instance.statically_loaded
    assert new_instance._from_files == include_role_instance._from_files
    assert new_instance._parent_role == include_role_instance._parent_role
    assert new_instance._role_name == include_role_instance._role_name
    assert new_instance._role_path == include_role_instance._role_path
