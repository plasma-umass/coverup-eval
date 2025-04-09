# file: lib/ansible/playbook/task.py:342-347
# asked: {"lines": [342, 347], "branches": []}
# gained: {"lines": [342, 347], "branches": []}

import pytest
from ansible.playbook.task import Task

class MockTemplar:
    pass

def test_post_validate_failed_when():
    task = Task()
    attr = "some_attr"
    value = "some_value"
    templar = MockTemplar()

    result = task._post_validate_failed_when(attr, value, templar)
    
    assert result == value
