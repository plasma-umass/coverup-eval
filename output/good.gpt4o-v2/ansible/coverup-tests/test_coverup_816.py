# file: lib/ansible/playbook/task.py:287-292
# asked: {"lines": [287, 292], "branches": []}
# gained: {"lines": [287, 292], "branches": []}

import pytest
from ansible.playbook.task import Task

def test_post_validate_loop():
    task = Task()
    attr = "loop"
    value = "some_value"
    templar = None  # Assuming templar is not used in the current implementation

    result = task._post_validate_loop(attr, value, templar)

    assert result == value
