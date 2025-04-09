# file: lib/ansible/playbook/play.py:243-262
# asked: {"lines": [243, 252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}
# gained: {"lines": [243, 252, 254, 255, 258, 259, 260, 262], "branches": [[254, 255], [254, 262], [255, 258], [255, 262], [258, 259], [258, 260]]}

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
def mock_role_from_include():
    role = MagicMock()
    role.from_include = True
    return role

def test_compile_roles_with_roles(mock_role):
    play = Play()
    play.roles = [mock_role]
    
    result = play._compile_roles()
    
    assert result == ['task1', 'task2']
    mock_role.compile.assert_called_once_with(play=play)

def test_compile_roles_with_roles_from_include(mock_role_from_include):
    play = Play()
    play.roles = [mock_role_from_include]
    
    result = play._compile_roles()
    
    assert result == []
    mock_role_from_include.compile.assert_not_called()

def test_compile_roles_no_roles():
    play = Play()
    play.roles = []
    
    result = play._compile_roles()
    
    assert result == []
