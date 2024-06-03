# file lib/ansible/plugins/callback/default.py:190-220
# lines []
# branches ['208->211']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task import Task

@pytest.fixture
def mock_task():
    task = MagicMock(spec=Task)
    task.no_log = False
    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    task._uuid = '1234-uuid'
    task.get_name.return_value = 'Test Task'
    task.check_mode = True
    return task

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._task_type_cache = {}
    cb._last_task_name = None
    cb.check_mode_markers = True
    cb._display = MagicMock()
    cb._display.verbosity = 1
    return cb

def test_print_task_banner_no_last_task_name(callback_module, mock_task):
    with patch('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._last_task_name = None
        callback_module._print_task_banner(mock_task)
        callback_module._display.banner.assert_called_once_with(
            u"TASK [Test Task arg1=value1, arg2=value2] [CHECK MODE]"
        )

def test_print_task_banner_with_last_task_name(callback_module, mock_task):
    with patch('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._last_task_name = 'Previous Task'
        callback_module._print_task_banner(mock_task)
        callback_module._display.banner.assert_called_once_with(
            u"TASK [Previous Task arg1=value1, arg2=value2] [CHECK MODE]"
        )
