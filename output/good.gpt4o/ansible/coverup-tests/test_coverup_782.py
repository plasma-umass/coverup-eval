# file lib/ansible/playbook/task.py:287-292
# lines [287, 292]
# branches []

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
def mock_templar():
    return MockTemplar()

def test_post_validate_loop(mock_templar):
    task = MockTask()
    attr = 'loop'
    value = ['item1', 'item2', 'item3']
    
    result = task._post_validate_loop(attr, value, mock_templar)
    
    assert result == value
