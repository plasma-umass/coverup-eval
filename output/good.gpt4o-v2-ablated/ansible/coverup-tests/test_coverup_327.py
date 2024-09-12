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

class TestTask:
    @pytest.fixture
    def task_instance(self):
        class TestTaskClass(Task, MockBase, MockConditional, MockTaggable, MockCollectionSearch):
            pass
        return TestTaskClass()

    def test_post_validate_loop(self, task_instance):
        attr = 'loop'
        value = [1, 2, 3]
        templar = MockTemplar()
        
        result = task_instance._post_validate_loop(attr, value, templar)
        
        assert result == value
