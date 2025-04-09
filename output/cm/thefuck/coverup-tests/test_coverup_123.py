# file thefuck/rules/tsuru_not_command.py:5-8
# lines [5, 6, 7, 8]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.tsuru_not_command import match

@pytest.fixture
def tsuru_error_output():
    return ' is not a tsuru command. See "tsuru help".\nDid you mean?\n\t'

def test_match_with_tsuru_not_command(tsuru_error_output):
    command = Command('tsuru fake-command', tsuru_error_output)
    assert match(command)

def test_not_match_with_tsuru_command(tsuru_error_output):
    command = Command('tsuru app-list', 'Listing apps...\n')
    assert not match(command)

def test_not_match_with_non_tsuru_command(tsuru_error_output):
    command = Command('git push', tsuru_error_output)
    assert not match(command)
