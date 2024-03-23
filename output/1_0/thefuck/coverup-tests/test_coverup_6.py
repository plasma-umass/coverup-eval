# file thefuck/rules/cargo.py:1-2
# lines [1, 2]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.cargo import match

def test_match():
    assert match(Command('cargo', '')) == True
    assert match(Command('cargo build', '')) == False
