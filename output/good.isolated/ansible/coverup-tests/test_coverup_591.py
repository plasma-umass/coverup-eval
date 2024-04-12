# file lib/ansible/playbook/task.py:141-146
# lines [141, 143, 144, 146]
# branches ['143->144', '143->146']

import pytest
from ansible.playbook.task import Task
from ansible.utils.sentinel import Sentinel

# Mocking the C._ACTION_META to include a test action
_ACTION_META = {'test_meta_action': True}

# Define the test function
def test_task_repr_meta(mocker):
    # Mock the Task.get_name method to return 'test_meta_action'
    mocker.patch.object(Task, 'get_name', return_value='test_meta_action')
    # Mock the C._ACTION_META to include a test action
    mocker.patch('ansible.playbook.task.C._ACTION_META', _ACTION_META)
    # Create a Task instance with the necessary _raw_params
    task = Task()
    task.args = {'_raw_params': 'test raw params'}

    # Assert that the __repr__ method returns the expected string for meta tasks
    assert repr(task) == "TASK: meta (test raw params)"

def test_task_repr_non_meta(mocker):
    # Mock the Task.get_name method to return 'non_meta_action'
    mocker.patch.object(Task, 'get_name', return_value='non_meta_action')
    # Create a Task instance
    task = Task()

    # Assert that the __repr__ method returns the expected string for non-meta tasks
    assert repr(task) == "TASK: non_meta_action"
