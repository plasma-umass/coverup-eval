# file thefuck/rules/git_rm_recursive.py:4-8
# lines [4, 5, 6, 7, 8]
# branches []

import pytest
from thefuck.rules.git_rm_recursive import match
from thefuck.types import Command

def test_git_rm_recursive_match():
    command = Command(script='git rm somefile', output="fatal: not removing 'somefile' recursively without -r")
    assert match(command)

    command = Command(script='git rm -r somefile', output="fatal: not removing 'somefile' recursively without -r")
    assert match(command)

    command = Command(script='git rm somefile', output="some other error")
    assert not match(command)

    command = Command(script='rm somefile', output="fatal: not removing 'somefile' recursively without -r")
    assert not match(command)
