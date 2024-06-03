# file lib/ansible/playbook/task.py:491-497
# lines [491, 492, 493, 494, 495, 496, 497]
# branches ['493->494', '493->497', '494->495', '494->496']

import pytest
from unittest.mock import Mock

from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

class TestTask:
    def test_get_first_parent_include_direct_parent(self):
        parent_task_include = Mock(spec=TaskInclude)
        task = Task()
        task._parent = parent_task_include

        result = task.get_first_parent_include()

        assert result == parent_task_include

    def test_get_first_parent_include_nested_parent(self):
        grandparent_task_include = Mock(spec=TaskInclude)
        parent_task = Mock(spec=Task)
        parent_task.get_first_parent_include.return_value = grandparent_task_include
        task = Task()
        task._parent = parent_task

        result = task.get_first_parent_include()

        assert result == grandparent_task_include

    def test_get_first_parent_include_no_parent(self):
        task = Task()
        task._parent = None

        result = task.get_first_parent_include()

        assert result is None
