# file thefuck/rules/git_commit_reset.py:4-6
# lines [4, 5, 6]
# branches []

import pytest
from thefuck.rules.git_commit_reset import match
from thefuck.types import Command

def test_match_commit_in_script_parts():
    command = Command('git commit -m "Initial commit"', ['git', 'commit', '-m', '"Initial commit"'])
    assert match(command)

def test_match_commit_not_in_script_parts():
    command = Command('git push origin master', ['git', 'push', 'origin', 'master'])
    assert not match(command)
