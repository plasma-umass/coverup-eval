# file: lib/ansible/plugins/callback/default.py:190-220
# asked: {"lines": [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220], "branches": [[200, 201], [200, 204], [208, 209], [208, 211], [211, 212], [211, 214], [217, 218], [217, 220]]}
# gained: {"lines": [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220], "branches": [[200, 201], [200, 204], [208, 209], [211, 212], [211, 214], [217, 218], [217, 220]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming CallbackModule and necessary imports are available from ansible.plugins.callback.default
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task():
    task = MagicMock()
    task.no_log = False
    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    task._uuid = '1234-uuid'
    task.check_mode = False
    task.get_name.return_value = 'Test Task'
    return task

def test_print_task_banner_no_log(callback_module, task, monkeypatch):
    monkeypatch.setattr('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._task_type_cache = {task._uuid: 'TASK'}
    callback_module._last_task_name = None
    callback_module._display = MagicMock()
    callback_module._display.verbosity = 1
    callback_module.check_mode_markers = True

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1, arg2=value2]')
    assert callback_module._last_task_banner == task._uuid

def test_print_task_banner_with_check_mode(callback_module, task, monkeypatch):
    monkeypatch.setattr('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._task_type_cache = {task._uuid: 'TASK'}
    callback_module._last_task_name = None
    callback_module._display = MagicMock()
    callback_module._display.verbosity = 1
    callback_module.check_mode_markers = True
    task.check_mode = True

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1, arg2=value2] [CHECK MODE]')
    assert callback_module._last_task_banner == task._uuid

def test_print_task_banner_no_args_display(callback_module, task, monkeypatch):
    monkeypatch.setattr('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', False)
    callback_module._task_type_cache = {task._uuid: 'TASK'}
    callback_module._last_task_name = None
    callback_module._display = MagicMock()
    callback_module._display.verbosity = 1
    callback_module.check_mode_markers = True

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task]')
    assert callback_module._last_task_banner == task._uuid

def test_print_task_banner_with_verbosity(callback_module, task, monkeypatch):
    monkeypatch.setattr('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._task_type_cache = {task._uuid: 'TASK'}
    callback_module._last_task_name = None
    callback_module._display = MagicMock()
    callback_module._display.verbosity = 2
    callback_module.check_mode_markers = True

    with patch.object(callback_module, '_print_task_path') as mock_print_task_path:
        callback_module._print_task_banner(task)
        mock_print_task_path.assert_called_once_with(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1, arg2=value2]')
    assert callback_module._last_task_banner == task._uuid
