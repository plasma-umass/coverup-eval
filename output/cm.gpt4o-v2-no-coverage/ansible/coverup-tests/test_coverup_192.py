# file: lib/ansible/plugins/callback/default.py:190-220
# asked: {"lines": [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220], "branches": [[200, 201], [200, 204], [208, 209], [208, 211], [211, 212], [211, 214], [217, 218], [217, 220]]}
# gained: {"lines": [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220], "branches": [[200, 201], [200, 204], [208, 209], [211, 212], [211, 214], [217, 218], [217, 220]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_print_task_banner_no_log(callback_module, monkeypatch):
    task = Mock()
    task.no_log = True
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False

    monkeypatch.setattr(callback_module, '_task_type_cache', {'1234': 'TASK'})
    monkeypatch.setattr(callback_module, '_last_task_name', None)
    monkeypatch.setattr(callback_module, '_display', Mock())
    monkeypatch.setattr(callback_module._display, 'verbosity', 1)

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task]')

def test_print_task_banner_display_args(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False

    monkeypatch.setattr(callback_module, '_task_type_cache', {'1234': 'TASK'})
    monkeypatch.setattr(callback_module, '_last_task_name', None)
    monkeypatch.setattr(callback_module, '_display', Mock())
    monkeypatch.setattr(callback_module._display, 'verbosity', 1)
    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1]')

def test_print_task_banner_check_mode(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = True

    monkeypatch.setattr(callback_module, '_task_type_cache', {'1234': 'TASK'})
    monkeypatch.setattr(callback_module, '_last_task_name', None)
    monkeypatch.setattr(callback_module, '_display', Mock())
    monkeypatch.setattr(callback_module._display, 'verbosity', 1)
    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)
    monkeypatch.setattr(callback_module, 'check_mode_markers', True, raising=False)

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1] [CHECK MODE]')

def test_print_task_banner_verbosity(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False

    monkeypatch.setattr(callback_module, '_task_type_cache', {'1234': 'TASK'})
    monkeypatch.setattr(callback_module, '_last_task_name', None)
    monkeypatch.setattr(callback_module, '_display', Mock())
    monkeypatch.setattr(callback_module._display, 'verbosity', 2)
    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)
    monkeypatch.setattr(callback_module, '_print_task_path', Mock())

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1]')
    callback_module._print_task_path.assert_called_once_with(task)
