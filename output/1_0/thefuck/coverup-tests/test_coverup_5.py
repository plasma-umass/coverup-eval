# file thefuck/rules/sl_ls.py:9-10
# lines [9, 10]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.sl_ls import match

def test_match():
    assert match(Command('sl', ''))
    assert not match(Command('ls', ''))
