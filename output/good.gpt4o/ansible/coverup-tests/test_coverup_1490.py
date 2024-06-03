# file lib/ansible/plugins/callback/junit.py:156-174
# lines []
# branches ['171->174']

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule, TaskData

@pytest.fixture
def mock_task():
    task = Mock()
    task._uuid = '1234-5678'
    task.get_name.return_value = 'test_task'
    task.get_path.return_value = '/path/to/task'
    task.action = 'test_action'
    task.no_log = False
    task.args = {}
    return task

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._task_data = {}
    cb._play_name = 'test_play'
    cb._hide_task_arguments = 'false'
    return cb

def test_start_task_without_args(callback_module, mock_task):
    callback_module._start_task(mock_task)
    
    assert '1234-5678' in callback_module._task_data
    task_data = callback_module._task_data['1234-5678']
    assert task_data.name == 'test_task'
    assert task_data.path == '/path/to/task'
    assert task_data.play == 'test_play'
    assert task_data.action == 'test_action'
