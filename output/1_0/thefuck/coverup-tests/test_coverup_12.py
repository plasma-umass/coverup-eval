# file thefuck/rules/remove_trailing_cedilla.py:6-7
# lines [6, 7]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.remove_trailing_cedilla import match

CEDILLA = 'ç'

@pytest.fixture
def command_with_cedilla():
    return Command('ls ç', '')

@pytest.fixture
def command_without_cedilla():
    return Command('ls', '')

def test_match_with_cedilla(command_with_cedilla):
    assert match(command_with_cedilla)

def test_match_without_cedilla(command_without_cedilla):
    assert not match(command_without_cedilla)
