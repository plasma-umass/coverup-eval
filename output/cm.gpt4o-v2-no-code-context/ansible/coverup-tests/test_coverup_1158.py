# file: lib/ansible/playbook/play.py:243-262
# asked: {"lines": [252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}
# gained: {"lines": [252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play

@pytest.fixture
def mock_role():
    role = MagicMock()
    role.from_include = False
    role.compile.return_value = ['task1', 'task2']
    return role

@pytest.fixture
def play_with_roles(mock_role):
    play = Play()
    play.roles = [mock_role]
    return play

@pytest.fixture
def play_with_include_role(mock_role):
    play = Play()
    mock_role.from_include = True
    play.roles = [mock_role]
    return play

def test_compile_roles_with_roles(play_with_roles):
    result = play_with_roles._compile_roles()
    assert result == ['task1', 'task2']
    play_with_roles.roles[0].compile.assert_called_once_with(play=play_with_roles)

def test_compile_roles_with_include_role(play_with_include_role):
    result = play_with_include_role._compile_roles()
    assert result == []
    play_with_include_role.roles[0].compile.assert_not_called()

def test_compile_roles_no_roles():
    play = Play()
    play.roles = []
    result = play._compile_roles()
    assert result == []
