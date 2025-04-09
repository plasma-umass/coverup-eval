# file: lib/ansible/playbook/task.py:342-347
# asked: {"lines": [347], "branches": []}
# gained: {"lines": [347], "branches": []}

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockTemplar:
    pass

class TestTask(Task, MockBase, MockConditional, MockTaggable, MockCollectionSearch):
    pass

@pytest.fixture
def task():
    return TestTask()

def test_post_validate_failed_when(task):
    attr = 'some_attr'
    value = 'some_value'
    templar = MockTemplar()
    
    result = task._post_validate_failed_when(attr, value, templar)
    
    assert result == value
