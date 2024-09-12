# file: httpie/context.py:60-86
# asked: {"lines": [81, 82, 84], "branches": [[79, 81], [82, 84], [82, 85]]}
# gained: {"lines": [81, 82, 84], "branches": [[79, 81], [82, 84], [82, 85]]}

import pytest
from unittest.mock import Mock, patch
from httpie.context import Environment
from colorama import AnsiToWin32

@pytest.fixture
def mock_is_windows(monkeypatch):
    monkeypatch.setattr('httpie.context.is_windows', True)

def test_environment_windows_with_ansi_to_win32(mock_is_windows):
    mock_stdout = Mock(spec=AnsiToWin32)
    mock_stdout.wrapped = Mock(encoding='cp1252')
    
    env = Environment(stdout=mock_stdout)
    
    assert env.stdout_encoding == 'cp1252'

def test_environment_windows_without_ansi_to_win32(mock_is_windows):
    mock_stdout = Mock(encoding='utf-8')
    
    env = Environment(stdout=mock_stdout)
    
    assert env.stdout_encoding == 'utf-8'
