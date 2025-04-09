# file: lib/ansible/plugins/callback/default.py:190-220
# asked: {"lines": [], "branches": [[208, 211]]}
# gained: {"lines": [], "branches": [[208, 211]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_print_task_banner_no_log(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False

    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._last_task_name = None
    callback_module.check_mode_markers = True
    callback_module._display = Mock()
    callback_module._display.verbosity = 1

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1]')
    assert callback_module._last_task_banner == '1234'

def test_print_task_banner_check_mode(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = True

    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._last_task_name = None
    callback_module.check_mode_markers = True
    callback_module._display = Mock()
    callback_module._display.verbosity = 1

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Test Task arg1=value1] [CHECK MODE]')
    assert callback_module._last_task_banner == '1234'

def test_print_task_banner_with_last_task_name(callback_module, monkeypatch):
    task = Mock()
    task.no_log = False
    task.args = {'arg1': 'value1'}
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    task.check_mode = False

    monkeypatch.setattr(C, 'DISPLAY_ARGS_TO_STDOUT', True)
    callback_module._last_task_name = 'Previous Task'
    callback_module.check_mode_markers = True
    callback_module._display = Mock()
    callback_module._display.verbosity = 1

    callback_module._print_task_banner(task)

    callback_module._display.banner.assert_called_once_with('TASK [Previous Task arg1=value1]')
    assert callback_module._last_task_banner == '1234'
