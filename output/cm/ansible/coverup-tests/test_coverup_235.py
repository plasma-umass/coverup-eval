# file lib/ansible/playbook/task.py:356-368
# lines [356, 357, 358, 359, 361, 363, 364, 365, 366, 368]
# branches ['358->359', '358->361', '363->364', '363->365', '365->366', '365->368']

import pytest
from unittest.mock import MagicMock

# Assuming the Task class is part of a module named ansible.playbook.task
from ansible.playbook.task import Task

@pytest.fixture
def mock_task():
    task = Task()
    task._parent = MagicMock()
    task.vars = {'tags': 'value1', 'when': 'value2', 'other_var': 'value3'}
    task._parent.get_vars.return_value = {'parent_var': 'value4', 'tags': 'value5', 'when': 'value6'}
    return task

def test_get_vars(mock_task):
    expected_vars = {'parent_var': 'value4', 'other_var': 'value3'}
    vars = mock_task.get_vars()
    assert vars == expected_vars
    assert 'tags' not in vars
    assert 'when' not in vars
    mock_task._parent.get_vars.assert_called_once()
