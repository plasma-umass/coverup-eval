# file thefuck/rules/sudo_command_from_user_path.py:11-15
# lines [11, 12, 13, 14, 15]
# branches ['13->exit', '13->14']

import pytest
from thefuck.types import Command
from thefuck.rules.sudo_command_from_user_path import match
from unittest.mock import Mock
from shutil import which

@pytest.fixture
def sudo_not_found_command():
    return Command('sudo ls', 'sudo: ls: command not found')

@pytest.fixture
def sudo_found_command():
    return Command('sudo ls', '')

@pytest.fixture(autouse=True)
def which_mock(mocker):
    return mocker.patch('shutil.which', return_value='/bin/ls')

def test_match_with_command_not_found(sudo_not_found_command, which_mock):
    assert match(sudo_not_found_command)
    which_mock.assert_called_once_with('ls')

def test_no_match_with_command_found(sudo_found_command, which_mock):
    assert not match(sudo_found_command)
    which_mock.assert_not_called()
