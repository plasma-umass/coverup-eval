# file: lib/ansible/playbook/play.py:207-228
# asked: {"lines": [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}
# gained: {"lines": [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def play_instance():
    return Play()

def test_load_roles_none_ds(play_instance, monkeypatch):
    # Mocking dependencies
    mock_load_list_of_roles = MagicMock(return_value=[])
    monkeypatch.setattr('ansible.playbook.play.load_list_of_roles', mock_load_list_of_roles)
    
    play_instance._variable_manager = MagicMock()
    play_instance._loader = MagicMock()
    play_instance.collections = MagicMock()
    play_instance.roles = []

    result = play_instance._load_roles('roles', None)
    
    assert result == []
    mock_load_list_of_roles.assert_called_once_with([], play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader, collection_search_list=play_instance.collections)

def test_load_roles_with_ds(play_instance, monkeypatch):
    # Mocking dependencies
    mock_load_list_of_roles = MagicMock(return_value=[MagicMock()])
    mock_role_load = MagicMock(return_value='role')
    monkeypatch.setattr('ansible.playbook.play.load_list_of_roles', mock_load_list_of_roles)
    monkeypatch.setattr('ansible.playbook.play.Role.load', mock_role_load)
    
    play_instance._variable_manager = MagicMock()
    play_instance._loader = MagicMock()
    play_instance.collections = MagicMock()
    play_instance.roles = []

    ds = [{'name': 'test_role'}]
    result = play_instance._load_roles('roles', ds)
    
    assert result == ['role']
    mock_load_list_of_roles.assert_called_once_with(ds, play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader, collection_search_list=play_instance.collections)
    mock_role_load.assert_called_once()

def test_load_roles_malformed_declaration(play_instance, monkeypatch):
    # Mocking dependencies
    mock_load_list_of_roles = MagicMock(side_effect=AssertionError)
    monkeypatch.setattr('ansible.playbook.play.load_list_of_roles', mock_load_list_of_roles)
    
    play_instance._variable_manager = MagicMock()
    play_instance._loader = MagicMock()
    play_instance.collections = MagicMock()
    play_instance.roles = []
    play_instance._ds = MagicMock()

    with pytest.raises(AnsibleParserError, match="A malformed role declaration was encountered."):
        play_instance._load_roles('roles', [{'name': 'test_role'}])
    
    mock_load_list_of_roles.assert_called_once()
