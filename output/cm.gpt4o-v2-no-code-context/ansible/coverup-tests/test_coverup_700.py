# file: lib/ansible/playbook/task.py:287-292
# asked: {"lines": [287, 292], "branches": []}
# gained: {"lines": [287, 292], "branches": []}

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

def test_post_validate_loop(mock_task):
    attr = 'loop'
    value = 'some_value'
    templar = MockTemplar()
    
    result = mock_task._post_validate_loop(attr, value, templar)
    
    assert result == value
