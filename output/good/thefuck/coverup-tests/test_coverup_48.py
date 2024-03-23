# file thefuck/system/unix.py:40-43
# lines [40, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from unittest.mock import patch
from thefuck.system.unix import open_command
from shutil import which

@pytest.fixture
def mock_find_executable(mocker):
    return mocker.patch('thefuck.system.unix.find_executable')

def test_open_command_with_xdg_open(mock_find_executable):
    mock_find_executable.return_value = '/usr/bin/xdg-open'
    arg = 'http://example.com'
    result = open_command(arg)
    assert result == 'xdg-open ' + arg

def test_open_command_without_xdg_open(mock_find_executable):
    mock_find_executable.return_value = None
    arg = 'http://example.com'
    result = open_command(arg)
    assert result == 'open ' + arg
