# file: lib/ansible/playbook/role/definition.py:48-60
# asked: {"lines": [48, 50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [48, 50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_role_definition_init():
    play = "test_play"
    role_basedir = "/test/role_basedir"
    variable_manager = "test_variable_manager"
    loader = "test_loader"
    collection_list = ["test_collection"]

    role_def = RoleDefinition(play, role_basedir, variable_manager, loader, collection_list)

    assert role_def._play == play
    assert role_def._role_basedir == role_basedir
    assert role_def._variable_manager == variable_manager
    assert role_def._loader == loader
    assert role_def._role_path is None
    assert role_def._role_collection is None
    assert role_def._role_params == {}
    assert role_def._collection_list == collection_list
