# file lib/ansible/playbook/role/definition.py:48-60
# lines [50, 52, 53, 54, 56, 57, 58, 59, 60]
# branches []

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition_cleanup(mocker):
    # Mock the Base, Conditional, and Taggable classes to prevent side effects
    mocker.patch('ansible.playbook.role.definition.Base')
    mocker.patch('ansible.playbook.role.definition.Conditional')
    mocker.patch('ansible.playbook.role.definition.Taggable')
    mocker.patch('ansible.playbook.role.definition.CollectionSearch')
    yield
    # No cleanup actions needed as the mocks will be automatically removed after the test

def test_role_definition_initialization(role_definition_cleanup):
    play = object()
    role_basedir = '/path/to/roles'
    variable_manager = object()
    loader = object()
    collection_list = ['collection1', 'collection2']

    role_def = RoleDefinition(
        play=play,
        role_basedir=role_basedir,
        variable_manager=variable_manager,
        loader=loader,
        collection_list=collection_list
    )

    assert role_def._play is play
    assert role_def._variable_manager is variable_manager
    assert role_def._loader is loader
    assert role_def._role_basedir == role_basedir
    assert role_def._role_params == {}
    assert role_def._collection_list == collection_list
