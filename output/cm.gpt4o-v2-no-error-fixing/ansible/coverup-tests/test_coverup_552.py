# file: lib/ansible/playbook/task.py:335-340
# asked: {"lines": [335, 340], "branches": []}
# gained: {"lines": [335, 340], "branches": []}

import pytest
from ansible.playbook.task import Task

def test_post_validate_changed_when():
    task = Task()
    attr = "changed_when"
    value = "some_value"
    templar = None  # Assuming templar is not used in the current implementation

    result = task._post_validate_changed_when(attr, value, templar)
    
    assert result == value
