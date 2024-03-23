# file lib/ansible/playbook/role_include.py:168-177
# lines [170, 171, 172, 173, 174, 175, 177]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_include_role(mocker):
    mock_role = IncludeRole()
    mock_role.statically_loaded = False
    mock_role._from_files = {'file1': 'path1', 'file2': 'path2'}
    mock_role._parent_role = 'parent_role'
    mock_role._role_name = 'role_name'
    mock_role._role_path = 'role_path'
    return mock_role

def test_include_role_copy(mock_include_role):
    # Copy the IncludeRole object
    new_include_role = mock_include_role.copy()

    # Assertions to ensure the copy has the same attributes as the original
    assert new_include_role.statically_loaded == mock_include_role.statically_loaded
    assert new_include_role._from_files == mock_include_role._from_files
    assert new_include_role._parent_role == mock_include_role._parent_role
    assert new_include_role._role_name == mock_include_role._role_name
    assert new_include_role._role_path == mock_include_role._role_path

    # Ensure that the _from_files dict was copied, not just referenced
    assert new_include_role._from_files is not mock_include_role._from_files
    assert new_include_role._from_files == {'file1': 'path1', 'file2': 'path2'}

    # Clean up is not necessary as no external state was modified
