# file lib/ansible/plugins/callback/default.py:190-220
# lines [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220]
# branches ['200->201', '200->204', '208->209', '208->211', '211->212', '211->214', '217->218', '217->220']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task import Task
from ansible import constants as C

@pytest.fixture
def mock_task():
    task = MagicMock(spec=Task)
    task.no_log = False
    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    task._uuid = '1234-uuid'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False
    return task

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._task_type_cache = {}
    cb._last_task_name = None
    cb._display = MagicMock()
    cb._display.verbosity = 1
    cb.check_mode_markers = True
    return cb

def test_print_task_banner(mock_task, callback_module):
    with patch.object(C, 'DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._print_task_banner(mock_task)
        callback_module._display.banner.assert_called_once_with(
            u"TASK [Test Task arg1=value1, arg2=value2]"
        )
        assert callback_module._last_task_banner == '1234-uuid'

def test_print_task_banner_no_args(mock_task, callback_module):
    mock_task.no_log = True
    with patch.object(C, 'DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._print_task_banner(mock_task)
        callback_module._display.banner.assert_called_once_with(
            u"TASK [Test Task]"
        )
        assert callback_module._last_task_banner == '1234-uuid'

def test_print_task_banner_check_mode(mock_task, callback_module):
    mock_task.check_mode = True
    with patch.object(C, 'DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._print_task_banner(mock_task)
        callback_module._display.banner.assert_called_once_with(
            u"TASK [Test Task arg1=value1, arg2=value2] [CHECK MODE]"
        )
        assert callback_module._last_task_banner == '1234-uuid'

def test_print_task_banner_verbosity(mock_task, callback_module):
    callback_module._display.verbosity = 2
    with patch.object(C, 'DISPLAY_ARGS_TO_STDOUT', True):
        with patch.object(callback_module, '_print_task_path') as mock_print_task_path:
            callback_module._print_task_banner(mock_task)
            mock_print_task_path.assert_called_once_with(mock_task)
            callback_module._display.banner.assert_called_once_with(
                u"TASK [Test Task arg1=value1, arg2=value2]"
            )
            assert callback_module._last_task_banner == '1234-uuid'
