# file thefuck/rules/tsuru_not_command.py:5-8
# lines [5, 6, 7, 8]
# branches []

import pytest
from thefuck.rules.tsuru_not_command import match
from thefuck.types import Command

@pytest.fixture
def tsuru_command():
    return Command('tsuru', 'some output')

def test_match_no_match(tsuru_command):
    tsuru_command.output = 'some unrelated output'
    assert not match(tsuru_command)

def test_match_partial_match(tsuru_command):
    tsuru_command.output = ' is not a tsuru command. See "tsuru help".'
    assert not match(tsuru_command)

def test_match_full_match(tsuru_command):
    tsuru_command.output = ' is not a tsuru command. See "tsuru help".\nDid you mean?\n\t'
    assert match(tsuru_command)
