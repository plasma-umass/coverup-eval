# file: lib/ansible/playbook/task.py:287-292
# asked: {"lines": [287, 292], "branches": []}
# gained: {"lines": [287, 292], "branches": []}

import pytest
from ansible.playbook.task import Task

@pytest.fixture
def task_instance():
    return Task()

def test_post_validate_loop(task_instance):
    attr = "some_attr"
    value = "some_value"
    templar = "some_templar"
    
    result = task_instance._post_validate_loop(attr, value, templar)
    
    assert result == value
