# file: lib/ansible/playbook/play.py:264-278
# asked: {"lines": [264, 270, 272, 273, 274, 275, 276, 278], "branches": [[272, 273], [272, 278], [273, 274], [273, 278], [274, 275], [274, 276]]}
# gained: {"lines": [264, 270, 272, 273, 274, 275, 276, 278], "branches": [[272, 273], [272, 278], [273, 274], [273, 278], [274, 275], [274, 276]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    play = Play()
    play.roles = []
    return play

def test_compile_roles_handlers_no_roles(play_instance):
    result = play_instance.compile_roles_handlers()
    assert result == []

def test_compile_roles_handlers_with_roles(play_instance):
    role_mock = MagicMock()
    role_mock.from_include = False
    role_mock.get_handler_blocks.return_value = ['handler1', 'handler2']
    
    play_instance.roles = [role_mock]
    
    result = play_instance.compile_roles_handlers()
    
    assert result == ['handler1', 'handler2']
    role_mock.get_handler_blocks.assert_called_once_with(play=play_instance)

def test_compile_roles_handlers_with_included_roles(play_instance):
    role_mock = MagicMock()
    role_mock.from_include = True
    
    play_instance.roles = [role_mock]
    
    result = play_instance.compile_roles_handlers()
    
    assert result == []
    role_mock.get_handler_blocks.assert_not_called()
