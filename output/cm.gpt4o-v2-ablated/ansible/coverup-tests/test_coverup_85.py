# file: lib/ansible/playbook/play.py:207-228
# asked: {"lines": [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}
# gained: {"lines": [207, 213, 214, 216, 217, 218, 219, 220, 222, 223, 224, 226, 228], "branches": [[213, 214], [213, 216], [223, 224], [223, 226]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play.collections = Mock()
    play._ds = Mock()
    play.roles = []
    return play

def test_load_roles_none_ds(play_instance):
    with patch('ansible.playbook.play.load_list_of_roles', return_value=[]):
        result = play_instance._load_roles('attr', None)
        assert result == []
        assert play_instance.roles == []

def test_load_roles_empty_ds(play_instance):
    with patch('ansible.playbook.play.load_list_of_roles', return_value=[]):
        result = play_instance._load_roles('attr', [])
        assert result == []
        assert play_instance.roles == []

def test_load_roles_with_roles(play_instance):
    mock_role_include = Mock()
    mock_role = Mock()
    with patch('ansible.playbook.play.load_list_of_roles', return_value=[mock_role_include]), \
         patch('ansible.playbook.play.Role.load', return_value=mock_role):
        result = play_instance._load_roles('attr', ['role1'])
        assert result == [mock_role]
        assert play_instance.roles == [mock_role]

def test_load_roles_malformed_declaration(play_instance):
    with patch('ansible.playbook.play.load_list_of_roles', side_effect=AssertionError):
        with pytest.raises(AnsibleParserError) as excinfo:
            play_instance._load_roles('attr', ['role1'])
        assert "A malformed role declaration was encountered." in str(excinfo.value)
