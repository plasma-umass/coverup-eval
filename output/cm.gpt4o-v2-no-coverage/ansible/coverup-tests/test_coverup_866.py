# file: lib/ansible/playbook/task.py:342-347
# asked: {"lines": [342, 347], "branches": []}
# gained: {"lines": [342, 347], "branches": []}

import pytest
from ansible.playbook.task import Task

@pytest.fixture
def task_instance():
    return Task()

def test_post_validate_failed_when(task_instance):
    attr = "some_attr"
    value = "some_value"
    templar = "some_templar"
    
    result = task_instance._post_validate_failed_when(attr, value, templar)
    
    assert result == value
