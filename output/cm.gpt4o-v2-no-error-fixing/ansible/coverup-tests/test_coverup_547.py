# file: lib/ansible/playbook/task.py:287-292
# asked: {"lines": [287, 292], "branches": []}
# gained: {"lines": [287, 292], "branches": []}

import pytest
from ansible.playbook.task import Task

class MockTemplar:
    pass

def test_post_validate_loop():
    task = Task()
    attr = "some_attr"
    value = "some_value"
    templar = MockTemplar()
    
    result = task._post_validate_loop(attr, value, templar)
    
    assert result == value
