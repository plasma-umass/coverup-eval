# file: lib/ansible/playbook/play.py:243-262
# asked: {"lines": [243, 252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}
# gained: {"lines": [243, 252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    play = Play()
    play.roles = []
    return play

def test_compile_roles_no_roles(play_instance):
    result = play_instance._compile_roles()
    assert result == []

def test_compile_roles_with_roles(monkeypatch):
    play = Play()
    role_mock = MagicMock()
    role_mock.from_include = False
    role_mock.compile.return_value = ['task1', 'task2']
    play.roles = [role_mock]

    result = play._compile_roles()
    assert result == ['task1', 'task2']
    role_mock.compile.assert_called_once_with(play=play)

def test_compile_roles_with_include_roles(monkeypatch):
    play = Play()
    role_mock = MagicMock()
    role_mock.from_include = True
    play.roles = [role_mock]

    result = play._compile_roles()
    assert result == []
    role_mock.compile.assert_not_called()
