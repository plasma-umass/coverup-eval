# file: lib/ansible/playbook/play.py:207-228
# asked: {"lines": [213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}
# gained: {"lines": [213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from unittest.mock import patch, MagicMock

@pytest.fixture
def play_instance():
    return Play()

def test_load_roles_with_none_ds(play_instance):
    with patch('ansible.playbook.play.load_list_of_roles', return_value=[]) as mock_load_list_of_roles:
        play_instance._variable_manager = MagicMock()
        play_instance._loader = MagicMock()
        play_instance.collections = MagicMock()
        play_instance.roles = []

        result = play_instance._load_roles('roles', None)

        mock_load_list_of_roles.assert_called_once_with([], play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader, collection_search_list=play_instance.collections)
        assert result == []
        assert play_instance.roles == []

def test_load_roles_with_malformed_role_declaration(play_instance):
    with patch('ansible.playbook.play.load_list_of_roles', side_effect=AssertionError) as mock_load_list_of_roles:
        play_instance._variable_manager = MagicMock()
        play_instance._loader = MagicMock()
        play_instance.collections = MagicMock()
        play_instance.roles = []
        play_instance._ds = MagicMock()

        with pytest.raises(AnsibleParserError, match="A malformed role declaration was encountered."):
            play_instance._load_roles('roles', [])

        mock_load_list_of_roles.assert_called_once_with([], play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader, collection_search_list=play_instance.collections)

def test_load_roles_success(play_instance):
    mock_role_include = MagicMock()
    mock_role = MagicMock()
    with patch('ansible.playbook.play.load_list_of_roles', return_value=[mock_role_include]) as mock_load_list_of_roles, \
         patch('ansible.playbook.role.Role.load', return_value=mock_role) as mock_role_load:
        
        play_instance._variable_manager = MagicMock()
        play_instance._loader = MagicMock()
        play_instance.collections = MagicMock()
        play_instance.roles = []

        result = play_instance._load_roles('roles', [{}])

        mock_load_list_of_roles.assert_called_once_with([{}], play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader, collection_search_list=play_instance.collections)
        mock_role_load.assert_called_once_with(mock_role_include, play=play_instance)
        assert result == [mock_role]
        assert play_instance.roles == [mock_role]
