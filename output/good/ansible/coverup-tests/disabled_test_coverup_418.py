# file lib/ansible/playbook/role/definition.py:48-60
# lines [48, 50, 52, 53, 54, 56, 57, 58, 59, 60]
# branches []

import pytest
from ansible.playbook.role.definition import RoleDefinition
from unittest.mock import MagicMock

# Test function to cover RoleDefinition.__init__
def test_role_definition_init(mocker):
    # Mock dependencies
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role_basedir = MagicMock()
    mock_collection_list = MagicMock()

    # Create instance of RoleDefinition
    role_definition = RoleDefinition(
        play=mock_play,
        role_basedir=mock_role_basedir,
        variable_manager=mock_variable_manager,
        loader=mock_loader,
        collection_list=mock_collection_list
    )

    # Assertions to verify postconditions
    assert role_definition._play is mock_play
    assert role_definition._variable_manager is mock_variable_manager
    assert role_definition._loader is mock_loader
    assert role_definition._role_basedir is mock_role_basedir
    assert role_definition._collection_list is mock_collection_list
    assert role_definition._role_path is None
    assert role_definition._role_collection is None
    assert role_definition._role_params == {}

    # Clean up
    mocker.stopall()
