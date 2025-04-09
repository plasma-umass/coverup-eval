# file thefuck/system/unix.py:40-43
# lines [41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from unittest.mock import patch
from shutil import which

# Assuming the function open_command is imported from thefuck.system.unix
from thefuck.system.unix import open_command

def test_open_command_xdg_open(mocker):
    mocker.patch('thefuck.system.unix.find_executable', return_value=True)
    arg = 'testfile.txt'
    result = open_command(arg)
    assert result == 'xdg-open testfile.txt'

def test_open_command_open(mocker):
    mocker.patch('thefuck.system.unix.find_executable', return_value=False)
    arg = 'testfile.txt'
    result = open_command(arg)
    assert result == 'open testfile.txt'
