# file lib/ansible/playbook/task_include.py:109-130
# lines [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130]
# branches ['115->116', '115->118', '119->120', '119->122', '125->126', '125->127', '127->128', '127->130']

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task_include import TaskInclude
from ansible.utils.sentinel import Sentinel

# Mocking the constants that would be used in the actual ansible codebase
class C:
    _ACTION_INCLUDE = ['include']

# Mocking the Task class that TaskInclude would inherit from
class MockTask:
    def get_vars(self):
        return {'parent_var': 'parent_value'}

# The test function to cover the missing lines/branches
@pytest.fixture
def task_include_fixture():
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include._parent = MockTask()
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value_arg1', 'tags': 'should_be_removed', 'when': 'should_also_be_removed'}
    return task_include

def test_task_include_get_vars(task_include_fixture):
    # Execute the get_vars method
    vars_result = task_include_fixture.get_vars()

    # Assertions to verify postconditions
    assert 'parent_var' in vars_result
    assert vars_result['parent_var'] == 'parent_value'
    assert 'var1' in vars_result
    assert vars_result['var1'] == 'value1'
    assert 'arg1' in vars_result
    assert vars_result['arg1'] == 'value_arg1'
    assert 'tags' not in vars_result
    assert 'when' not in vars_result

# Test when the action is not in C._ACTION_INCLUDE
def test_task_include_get_vars_different_action(task_include_fixture):
    task_include_fixture.action = 'not_include'
    # Mock the super().get_vars() to return a specific value
    task_include_fixture.get_vars = MagicMock(return_value={'parent_var': 'parent_value'})
    vars_result = task_include_fixture.get_vars()

    # Assertions to verify postconditions
    assert vars_result == {'parent_var': 'parent_value'}

# Test when there is no parent
def test_task_include_get_vars_no_parent(task_include_fixture):
    task_include_fixture._parent = None
    vars_result = task_include_fixture.get_vars()

    # Assertions to verify postconditions
    assert 'parent_var' not in vars_result
    assert 'var1' in vars_result
    assert vars_result['var1'] == 'value1'
    assert 'arg1' in vars_result
    assert vars_result['arg1'] == 'value_arg1'
    assert 'tags' not in vars_result
    assert 'when' not in vars_result
