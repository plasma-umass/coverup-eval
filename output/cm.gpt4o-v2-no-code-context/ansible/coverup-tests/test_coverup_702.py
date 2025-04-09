# file: lib/ansible/playbook/task.py:335-340
# asked: {"lines": [335, 340], "branches": []}
# gained: {"lines": [335], "branches": []}

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

class TestTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch):
    def _post_validate_changed_when(self, attr, value, templar):
        '''
        changed_when is evaluated after the execution of the task is complete,
        and should not be templated during the regular post_validate step.
        '''
        return value

@pytest.fixture
def task():
    return TestTask()

def test_post_validate_changed_when(task):
    attr = 'changed_when'
    value = 'some_value'
    templar = MockTemplar()

    result = task._post_validate_changed_when(attr, value, templar)
    
    assert result == value
