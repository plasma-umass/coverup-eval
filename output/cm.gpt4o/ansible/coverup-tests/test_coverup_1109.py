# file lib/ansible/playbook/task.py:356-368
# lines [357, 358, 359, 361, 363, 364, 365, 366, 368]
# branches ['358->359', '358->361', '363->364', '363->365', '365->366', '365->368']

import pytest
from unittest.mock import Mock

# Assuming the Task class and its dependencies are imported from ansible.playbook.task
from ansible.playbook.task import Task

class TestTask:
    @pytest.fixture
    def task_with_parent(self):
        parent_task = Mock()
        parent_task.get_vars.return_value = {'parent_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
        task = Task()
        task._parent = parent_task
        task.vars = {'task_var': 'value'}
        return task

    @pytest.fixture
    def task_without_parent(self):
        task = Task()
        task._parent = None
        task.vars = {'task_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
        return task

    def test_get_vars_with_parent(self, task_with_parent):
        result = task_with_parent.get_vars()
        assert 'parent_var' in result
        assert 'task_var' in result
        assert 'tags' not in result
        assert 'when' not in result

    def test_get_vars_without_parent(self, task_without_parent):
        result = task_without_parent.get_vars()
        assert 'task_var' in result
        assert 'tags' not in result
        assert 'when' not in result
