# file thefuck/rules/pacman_invalid_option.py:7-12
# lines [7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.pacman_invalid_option import match
from unittest.mock import Mock

@pytest.fixture
def pacman_invalid_option():
    return "error: invalid option '-x'"

@pytest.fixture
def pacman_script():
    return "pacman -sx package"

@pytest.fixture
def no_pacman_script():
    return "apt-get install package"

def test_match_with_pacman_invalid_option(mocker, pacman_invalid_option, pacman_script):
    mocker.patch('thefuck.rules.pacman_invalid_option.for_app', return_value=True)
    command = Command(script=pacman_script, output=pacman_invalid_option)
    assert match(command)

def test_no_match_with_pacman_invalid_option(mocker, pacman_invalid_option, no_pacman_script):
    mocker.patch('thefuck.rules.pacman_invalid_option.for_app', return_value=False)
    command = Command(script=no_pacman_script, output=pacman_invalid_option)
    assert not match(command)

def test_no_match_with_no_pacman_invalid_option(mocker, pacman_script):
    mocker.patch('thefuck.rules.pacman_invalid_option.for_app', return_value=True)
    command = Command(script=pacman_script, output="some other error")
    assert not match(command)
