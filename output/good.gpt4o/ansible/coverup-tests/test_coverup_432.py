# file lib/ansible/playbook/role/definition.py:48-60
# lines [48, 50, 52, 53, 54, 56, 57, 58, 59, 60]
# branches []

import pytest
from unittest import mock
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def mock_base_classes(mocker):
    mocker.patch('ansible.playbook.role.definition.Base', autospec=True)
    mocker.patch('ansible.playbook.role.definition.Conditional', autospec=True)
    mocker.patch('ansible.playbook.role.definition.Taggable', autospec=True)
    mocker.patch('ansible.playbook.role.definition.CollectionSearch', autospec=True)

def test_role_definition_initialization(mock_base_classes):
    play = mock.Mock()
    role_basedir = '/path/to/role'
    variable_manager = mock.Mock()
    loader = mock.Mock()
    collection_list = ['collection1', 'collection2']

    role_def = RoleDefinition(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    assert role_def._play == play
    assert role_def._variable_manager == variable_manager
    assert role_def._loader == loader
    assert role_def._role_basedir == role_basedir
    assert role_def._role_path is None
    assert role_def._role_collection is None
    assert role_def._role_params == {}
    assert role_def._collection_list == collection_list
