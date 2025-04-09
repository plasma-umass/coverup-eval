# file: lib/ansible/playbook/role_include.py:59-66
# asked: {"lines": [59, 61, 63, 64, 65, 66], "branches": []}
# gained: {"lines": [59, 61, 63, 64, 65, 66], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_task_include(mocker):
    return mocker.Mock()

def test_include_role_initialization(mock_task_include):
    block = mock_task_include
    role = mock_task_include
    task_include = mock_task_include

    include_role = IncludeRole(block=block, role=role, task_include=task_include)

    assert include_role._from_files == {}
    assert include_role._parent_role == role
    assert include_role._role_name is None
    assert include_role._role_path is None

def test_include_role_initialization_no_params():
    include_role = IncludeRole()

    assert include_role._from_files == {}
    assert include_role._parent_role is None
    assert include_role._role_name is None
    assert include_role._role_path is None
