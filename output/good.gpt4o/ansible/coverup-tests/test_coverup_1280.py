# file lib/ansible/plugins/callback/junit.py:156-174
# lines []
# branches ['169->174', '171->174']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule, TaskData

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_task():
    task = Mock()
    task._uuid = '1234'
    task.get_name.return_value = 'test_task'
    task.get_path.return_value = '/path/to/task'
    task.action = 'test_action'
    task.no_log = False
    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    return task

def test_start_task_with_args(callback_module, mock_task):
    callback_module._task_data = {}
    callback_module._play_name = 'test_play'
    callback_module._hide_task_arguments = 'false'

    callback_module._start_task(mock_task)

    assert '1234' in callback_module._task_data
    task_data = callback_module._task_data['1234']
    assert task_data.name == 'test_task arg1=value1, arg2=value2'
    assert task_data.path == '/path/to/task'
    assert task_data.play == 'test_play'
    assert task_data.action == 'test_action'

def test_start_task_no_args(callback_module, mock_task):
    callback_module._task_data = {}
    callback_module._play_name = 'test_play'
    callback_module._hide_task_arguments = 'true'

    callback_module._start_task(mock_task)

    assert '1234' in callback_module._task_data
    task_data = callback_module._task_data['1234']
    assert task_data.name == 'test_task'
    assert task_data.path == '/path/to/task'
    assert task_data.play == 'test_play'
    assert task_data.action == 'test_action'
