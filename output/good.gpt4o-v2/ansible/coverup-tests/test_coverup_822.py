# file: lib/ansible/playbook/task.py:335-340
# asked: {"lines": [335, 340], "branches": []}
# gained: {"lines": [335, 340], "branches": []}

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

class MockTemplar:
    def template(self, value, **kwargs):
        return value

@pytest.fixture
def task():
    return Task()

def test_post_validate_changed_when(task):
    attr = "changed_when"
    value = "some_value"
    templar = MockTemplar()

    result = task._post_validate_changed_when(attr, value, templar)
    
    assert result == value
