# file: lib/ansible/playbook/task.py:335-340
# asked: {"lines": [340], "branches": []}
# gained: {"lines": [340], "branches": []}

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

class TestTask:
    @pytest.fixture
    def task(self):
        class MockTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
            pass
        return MockTask()

    def test_post_validate_changed_when(self, task):
        attr = 'changed_when'
        value = 'some_value'
        templar = MockTemplar()
        
        result = task._post_validate_changed_when(attr, value, templar)
        
        assert result == value
