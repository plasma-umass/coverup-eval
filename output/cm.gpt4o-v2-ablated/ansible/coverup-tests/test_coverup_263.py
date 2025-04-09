# file: lib/ansible/plugins/callback/default.py:228-230
# asked: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}
# gained: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
from unittest.mock import MagicMock

@pytest.fixture
def callback_module(monkeypatch):
    display = Display()
    monkeypatch.setattr(display, 'display', MagicMock())
    monkeypatch.setattr('ansible.plugins.callback.default.C.COLOR_OK', 'green')
    
    class TestCallbackModule(CallbackModule):
        def __init__(self):
            self._display = display
            self._options = {'show_per_host_start': False}
        
        def get_option(self, option):
            return self._options.get(option, None)
    
    return TestCallbackModule()

def test_v2_runner_on_start_show_per_host_start_true(callback_module):
    callback_module._options['show_per_host_start'] = True
    callback_module.v2_runner_on_start('localhost', 'test_task')
    callback_module._display.display.assert_called_once_with(" [started test_task on localhost]", color='green')

def test_v2_runner_on_start_show_per_host_start_false(callback_module):
    callback_module._options['show_per_host_start'] = False
    callback_module.v2_runner_on_start('localhost', 'test_task')
    callback_module._display.display.assert_not_called()
