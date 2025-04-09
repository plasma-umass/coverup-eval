# file lib/ansible/playbook/task_include.py:109-130
# lines [115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130]
# branches ['115->116', '115->118', '119->120', '119->122', '125->126', '125->127', '127->128', '127->130']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.utils.sentinel import Sentinel
from unittest.mock import MagicMock

# Mock the constants that are used within the TaskInclude class
C = MagicMock()
C._ACTION_INCLUDE = ['include']

@pytest.fixture
def task_include_fixture(mocker):
    # Mock the TaskInclude class's parent and action attributes
    task_include = TaskInclude()
    task_include._parent = MagicMock()
    task_include._parent.get_vars.return_value = {'parent_var': 'parent_value'}
    task_include.action = 'include'
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value_arg1'}
    mocker.patch.object(task_include, '_parent')
    mocker.patch('ansible.playbook.task_include.C', C)
    return task_include

def test_task_include_get_vars(task_include_fixture):
    # Test the get_vars method to ensure it includes args and vars
    task_include_fixture._parent.get_vars.return_value = {'parent_var': 'parent_value'}
    all_vars = task_include_fixture.get_vars()

    # Assertions to check if the vars are correctly updated
    assert all_vars['parent_var'] == 'parent_value'
    assert all_vars['var1'] == 'value1'
    assert all_vars['arg1'] == 'value_arg1'
    assert 'tags' not in all_vars
    assert 'when' not in all_vars

    # Clean up after the test
    task_include_fixture._parent.get_vars.assert_called_once()
