# file: lib/ansible/playbook/task.py:349-354
# asked: {"lines": [349, 354], "branches": []}
# gained: {"lines": [349, 354], "branches": []}

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

class MockTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
    pass

@pytest.fixture
def mock_task():
    return MockTask()

def test_post_validate_until(mock_task):
    attr = 'until'
    value = 'some_value'
    templar = MockTemplar()
    
    result = mock_task._post_validate_until(attr, value, templar)
    
    assert result == value
