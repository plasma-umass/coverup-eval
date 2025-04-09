# file: lib/ansible/playbook/role_include.py:59-66
# asked: {"lines": [59, 61, 63, 64, 65, 66], "branches": []}
# gained: {"lines": [59, 61, 63, 64, 65, 66], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.task_include import TaskInclude

class MockTaskInclude(TaskInclude):
    def __init__(self, block=None, role=None, task_include=None):
        super(MockTaskInclude, self).__init__(block=block, role=role, task_include=task_include)

@pytest.fixture
def mock_task_include(monkeypatch):
    def mock_init(self, block=None, role=None, task_include=None):
        self.block = block
        self.role = role
        self.task_include = task_include
        self.statically_loaded = False

    monkeypatch.setattr(TaskInclude, "__init__", mock_init)

def test_include_role_init(mock_task_include):
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"

    include_role = IncludeRole(block=block, role=role, task_include=task_include)

    assert include_role.block == block
    assert include_role._parent_role == role
    assert include_role._role_name is None
    assert include_role._role_path is None
    assert include_role._from_files == {}
