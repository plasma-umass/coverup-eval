# file: lib/ansible/playbook/play.py:264-278
# asked: {"lines": [270, 272, 273, 274, 275, 276, 278], "branches": [[272, 273], [272, 278], [273, 274], [273, 278], [274, 275], [274, 276]]}
# gained: {"lines": [270, 272, 273, 274, 276, 278], "branches": [[272, 273], [272, 278], [273, 274], [273, 278], [274, 276]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play  # Ensure the Play class is imported correctly

@pytest.fixture
def mock_role():
    role = MagicMock()
    role.from_include = False
    role.get_handler_blocks.return_value = ['handler1', 'handler2']
    return role

@pytest.fixture
def play_with_roles(mock_role):
    play = Play()
    play.roles = [mock_role]
    return play

@pytest.fixture
def play_without_roles():
    play = Play()
    play.roles = []
    return play

def test_compile_roles_handlers_with_roles(play_with_roles, mock_role):
    result = play_with_roles.compile_roles_handlers()
    assert result == ['handler1', 'handler2']
    mock_role.get_handler_blocks.assert_called_once_with(play=play_with_roles)

def test_compile_roles_handlers_without_roles(play_without_roles):
    result = play_without_roles.compile_roles_handlers()
    assert result == []
