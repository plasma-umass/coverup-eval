# file lib/ansible/playbook/role_include.py:59-66
# lines [59, 61, 63, 64, 65, 66]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.role import Role
from unittest.mock import Mock

# Assuming that the IncludeRole class is part of a larger module that we're testing

@pytest.fixture
def mock_role():
    mock_role = Mock(spec=Role)
    return mock_role

@pytest.fixture
def mock_task_include():
    mock_task_include = Mock()
    return mock_task_include

@pytest.fixture
def mock_block():
    mock_block = Mock()
    return mock_block

def test_include_role_initialization(mock_role, mock_task_include, mock_block):
    # Instantiate IncludeRole with all parameters
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)
    
    # Assertions to ensure that the IncludeRole object is initialized correctly
    assert include_role._parent_role == mock_role
    assert include_role._role_name is None
    assert include_role._role_path is None
    assert isinstance(include_role._from_files, dict)
    assert include_role._from_files == {}

    # Clean up
    del include_role
