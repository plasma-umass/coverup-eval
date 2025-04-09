# file: lib/ansible/plugins/callback/default.py:228-230
# asked: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}
# gained: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from unittest.mock import MagicMock

@pytest.fixture
def callback_module(monkeypatch):
    display = Display()
    monkeypatch.setattr(display, 'display', MagicMock())
    module = CallbackModule()
    monkeypatch.setattr(module, '_display', display)
    return module

def test_v2_runner_on_start_show_per_host_start(callback_module, monkeypatch):
    monkeypatch.setattr(callback_module, 'get_option', lambda x: True if x == 'show_per_host_start' else None)
    host = 'localhost'
    task = 'test_task'
    callback_module.v2_runner_on_start(host, task)
    callback_module._display.display.assert_called_once_with(" [started %s on %s]" % (task, host), color='green')

def test_v2_runner_on_start_no_show_per_host_start(callback_module, monkeypatch):
    monkeypatch.setattr(callback_module, 'get_option', lambda x: False if x == 'show_per_host_start' else None)
    host = 'localhost'
    task = 'test_task'
    callback_module.v2_runner_on_start(host, task)
    callback_module._display.display.assert_not_called()
