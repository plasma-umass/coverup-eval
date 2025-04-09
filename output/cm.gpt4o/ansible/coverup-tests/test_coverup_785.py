# file lib/ansible/playbook/task.py:342-347
# lines [342, 347]
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

class TestTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
    pass

@pytest.fixture
def mock_templar():
    return MockTemplar()

def test_post_validate_failed_when(mock_templar):
    task = TestTask()
    attr = 'some_attr'
    value = 'some_value'
    
    result = task._post_validate_failed_when(attr, value, mock_templar)
    
    assert result == value
