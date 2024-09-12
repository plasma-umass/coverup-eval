# file: lib/ansible/playbook/role/definition.py:48-60
# asked: {"lines": [50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [50, 52, 53, 54, 56, 57, 58, 59, 60], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

class MockBase:
    def __init__(self):
        pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

@pytest.fixture
def mock_classes(monkeypatch):
    monkeypatch.setattr('ansible.playbook.role.definition.Base', MockBase)
    monkeypatch.setattr('ansible.playbook.role.definition.Conditional', MockConditional)
    monkeypatch.setattr('ansible.playbook.role.definition.Taggable', MockTaggable)
    monkeypatch.setattr('ansible.playbook.role.definition.CollectionSearch', MockCollectionSearch)

def test_role_definition_initialization(mock_classes):
    play = 'mock_play'
    role_basedir = 'mock_role_basedir'
    variable_manager = 'mock_variable_manager'
    loader = 'mock_loader'
    collection_list = ['mock_collection']

    role_def = RoleDefinition(play, role_basedir, variable_manager, loader, collection_list)

    assert role_def._play == play
    assert role_def._role_basedir == role_basedir
    assert role_def._variable_manager == variable_manager
    assert role_def._loader == loader
    assert role_def._collection_list == collection_list
    assert role_def._role_path is None
    assert role_def._role_collection is None
    assert role_def._role_params == {}
