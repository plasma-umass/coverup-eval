# file: lib/ansible/plugins/callback/default.py:190-220
# asked: {"lines": [201, 202, 209, 214, 218], "branches": [[200, 201], [208, 209], [211, 214], [217, 218]]}
# gained: {"lines": [201, 202, 209, 214, 218], "branches": [[200, 201], [208, 209], [211, 214], [217, 218]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def task():
    task = MagicMock()
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

def test_print_task_banner_args_displayed(callback_module, task):
    with patch.object(C, 'DISPLAY_ARGS_TO_STDOUT', True):
        callback_module._print_task_banner(task)
        callback_module._display.banner.assert_called_once_with(u"TASK [Test Task arg1=value1, arg2=value2]")

def test_print_task_banner_no_task_name(callback_module, task):
    callback_module._last_task_name = None
    callback_module._print_task_banner(task)
    callback_module._display.banner.assert_called_once_with(u"TASK [Test Task]")

def test_print_task_banner_check_mode(callback_module, task):
    task.check_mode = True
    callback_module._print_task_banner(task)
    callback_module._display.banner.assert_called_once_with(u"TASK [Test Task] [CHECK MODE]")

def test_print_task_banner_verbosity(callback_module, task):
    callback_module._display.verbosity = 2
    callback_module._print_task_banner(task)
    callback_module._display.banner.assert_called_once_with(u"TASK [Test Task]")
    callback_module._display.banner.reset_mock()
    callback_module._print_task_path = MagicMock()
    callback_module._print_task_banner(task)
    callback_module._print_task_path.assert_called_once_with(task)
