# file thefuck/rules/git_push_pull.py:6-14
# lines [6, 7, 8, 9, 10, 11, 12, 13, 14]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_push_pull import match

@pytest.fixture
def push_rejected_behind_output():
    return ("! [rejected]        master -> master (fetch first)\n"
            "error: failed to push some refs to 'git@example.com:repo.git'\n"
            "hint: Updates were rejected because the tip of your current branch is behind\n")

@pytest.fixture
def push_rejected_remote_changes_output():
    return ("! [rejected]        master -> master (fetch first)\n"
            "error: failed to push some refs to 'git@example.com:repo.git'\n"
            "hint: Updates were rejected because the remote contains work that you do\n")

def test_match_push_rejected_behind(push_rejected_behind_output):
    command = Command('git push origin master', push_rejected_behind_output)
    assert match(command)

def test_match_push_rejected_remote_changes(push_rejected_remote_changes_output):
    command = Command('git push origin master', push_rejected_remote_changes_output)
    assert match(command)
