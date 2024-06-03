# file thefuck/rules/pacman_invalid_option.py:7-12
# lines [7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.rules.pacman_invalid_option import match
from thefuck.types import Command

@pytest.fixture
def mock_command():
    return Command(script='pacman -s', output="error: invalid option '-s'")

def test_match_valid_option(mock_command):
    assert match(mock_command)

def test_match_invalid_option():
    command = Command(script='pacman -x', output="error: invalid option '-x'")
    assert not match(command)

def test_match_no_error():
    command = Command(script='pacman -s', output="some other output")
    assert not match(command)
