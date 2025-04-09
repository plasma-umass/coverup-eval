# file: lib/ansible/playbook/task.py:342-347
# asked: {"lines": [342, 347], "branches": []}
# gained: {"lines": [342, 347], "branches": []}

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
def task_instance():
    return TestTask()

def test_post_validate_failed_when(task_instance):
    attr = 'failed_when'
    value = 'some_value'
    templar = MockTemplar()

    result = task_instance._post_validate_failed_when(attr, value, templar)
    
    assert result == value
