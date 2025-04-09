# file lib/ansible/playbook/play.py:207-228
# lines [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228]
# branches ['213->214', '213->216', '223->224', '223->226']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.role_include import RoleInclude
from ansible.playbook.role import Role
from unittest.mock import MagicMock

# Mocking the load_list_of_roles function to raise an AssertionError
def mock_load_list_of_roles(ds, play, variable_manager, loader, collection_search_list):
    raise AssertionError("malformed role declaration")

# Mocking the Role.load function to return a simple mock object
def mock_role_load(ri, play):
    return MagicMock()

# Test function to cover the exception branch in _load_roles
def test_load_roles_with_malformed_declaration(mocker):
    # Mocking the load_list_of_roles to raise an AssertionError
    mocker.patch('ansible.playbook.play.load_list_of_roles', side_effect=mock_load_list_of_roles)
    # Mocking the Role.load to return a mock object
    mocker.patch('ansible.playbook.role.Role.load', side_effect=mock_role_load)

    play = Play()

    # Setting up the necessary attributes for the Play object
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play.collections = []
    play._ds = MagicMock()  # Add this line to set the _ds attribute

    # The malformed role declaration should raise an AnsibleParserError
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_roles('roles', [{'role': 'invalid_role'}])

    assert "A malformed role declaration was encountered." in str(excinfo.value), "The exception message should indicate a malformed role declaration"

# Test function to cover the normal execution branch in _load_roles
def test_load_roles_with_valid_declaration(mocker):
    # Mocking the load_list_of_roles to return a list of RoleInclude objects
    mocker.patch('ansible.playbook.play.load_list_of_roles', return_value=[RoleInclude()])
    # Mocking the Role.load to return a mock object
    mocker.patch('ansible.playbook.role.Role.load', side_effect=mock_role_load)

    play = Play()

    # Setting up the necessary attributes for the Play object
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play.collections = []
    play._ds = MagicMock()  # Add this line to set the _ds attribute

    # The valid role declaration should not raise an exception and should return a list of roles
    roles = play._load_roles('roles', [{'role': 'valid_role'}])

    assert isinstance(roles, list), "The returned object should be a list"
    assert len(roles) == 1, "The list should contain one role"
    assert isinstance(roles[0], MagicMock), "The list should contain mock Role objects"
