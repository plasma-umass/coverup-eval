# file thefuck/rules/git_push_pull.py:6-14
# lines [8, 9, 10, 11, 12, 13, 14]
# branches []

import pytest
from thefuck.rules.git_push_pull import match
from thefuck.types import Command

def test_match_push_rejected():
    command = Command(
        script='git push',
        output=(
            '! [rejected] master -> master (fetch first)\n'
            'error: failed to push some refs to \'origin\'\n'
            'hint: Updates were rejected because the tip of your current branch is behind\n'
            'hint: its remote counterpart. Integrate the remote changes (e.g.\n'
            'hint: \'git pull ...\') before pushing again.\n'
        )
    )
    assert match(command)

def test_match_push_rejected_remote_contains_work():
    command = Command(
        script='git push',
        output=(
            '! [rejected] master -> master (fetch first)\n'
            'error: failed to push some refs to \'origin\'\n'
            'hint: Updates were rejected because the remote contains work that you do\n'
            'hint: not have locally. This is usually caused by another repository pushing\n'
            'hint: to the same ref. You may want to first integrate the remote changes\n'
            'hint: (e.g., \'git pull ...\') before pushing again.\n'
        )
    )
    assert match(command)
