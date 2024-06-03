# file lib/ansible/playbook/play.py:207-228
# lines [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228]
# branches ['213->214', '213->216', '223->224', '223->226']

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_roles(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_roles')

@pytest.fixture
def mock_role(mocker):
    return mocker.patch('ansible.playbook.play.Role')

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play.collections = Mock()
    play._ds = Mock()
    play.roles = []
    return play

def test_load_roles_none_ds(play_instance, mock_load_list_of_roles, mock_role):
    mock_load_list_of_roles.return_value = []
    result = play_instance._load_roles('attr', None)
    assert result == []
    mock_load_list_of_roles.assert_called_once_with([], play=play_instance, variable_manager=play_instance._variable_manager,
                                                    loader=play_instance._loader, collection_search_list=play_instance.collections)

def test_load_roles_with_ds(play_instance, mock_load_list_of_roles, mock_role):
    mock_load_list_of_roles.return_value = ['role1', 'role2']
    mock_role.load.side_effect = ['loaded_role1', 'loaded_role2']
    result = play_instance._load_roles('attr', ['role1', 'role2'])
    assert result == ['loaded_role1', 'loaded_role2']
    mock_load_list_of_roles.assert_called_once_with(['role1', 'role2'], play=play_instance, variable_manager=play_instance._variable_manager,
                                                    loader=play_instance._loader, collection_search_list=play_instance.collections)
    assert play_instance.roles == ['loaded_role1', 'loaded_role2']

def test_load_roles_malformed_role(play_instance, mock_load_list_of_roles):
    mock_load_list_of_roles.side_effect = AssertionError
    with pytest.raises(AnsibleParserError, match="A malformed role declaration was encountered."):
        play_instance._load_roles('attr', ['malformed_role'])
