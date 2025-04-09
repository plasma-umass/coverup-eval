# file: lib/ansible/playbook/role/definition.py:48-60
# asked: {"lines": [48, 50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [48, 50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    return RoleDefinition(play='test_play', role_basedir='/test/role/basedir', variable_manager='test_variable_manager', loader='test_loader', collection_list=['test_collection'])

def test_role_definition_init(role_definition):
    assert role_definition._play == 'test_play'
    assert role_definition._variable_manager == 'test_variable_manager'
    assert role_definition._loader == 'test_loader'
    assert role_definition._role_path is None
    assert role_definition._role_collection is None
    assert role_definition._role_basedir == '/test/role/basedir'
    assert role_definition._role_params == {}
    assert role_definition._collection_list == ['test_collection']
