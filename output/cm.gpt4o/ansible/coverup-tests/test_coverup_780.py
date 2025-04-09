# file lib/ansible/playbook/task.py:335-340
# lines [335, 340]
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

class MockTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
    pass

@pytest.fixture
def mock_templar(mocker):
    return mocker.Mock(spec=Templar)

def test_post_validate_changed_when(mock_templar):
    task = MockTask()
    attr = 'changed_when'
    value = 'some_value'
    
    result = task._post_validate_changed_when(attr, value, mock_templar)
    
    assert result == value
