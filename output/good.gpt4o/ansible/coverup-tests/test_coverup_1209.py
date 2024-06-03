# file lib/ansible/playbook/task.py:141-146
# lines [143, 144, 146]
# branches ['143->144', '143->146']

import pytest
from unittest.mock import Mock, patch

# Assuming the Task class and C._ACTION_META are imported from the appropriate module
from ansible.playbook.task import Task
import ansible.constants as C

@pytest.fixture
def mock_task():
    task = Task()
    task.args = {'_raw_params': 'some_params'}
    return task

def test_task_repr_meta(mock_task, mocker):
    mocker.patch.object(mock_task, 'get_name', return_value='meta_action')
    mocker.patch.object(C, '_ACTION_META', ['meta_action'])
    
    result = repr(mock_task)
    assert result == "TASK: meta (some_params)"

def test_task_repr_non_meta(mock_task, mocker):
    mocker.patch.object(mock_task, 'get_name', return_value='normal_action')
    mocker.patch.object(C, '_ACTION_META', [])
    
    result = repr(mock_task)
    assert result == "TASK: normal_action"
