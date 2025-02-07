# file: lib/ansible/plugins/callback/default.py:228-230
# asked: {"lines": [], "branches": [[229, 0]]}
# gained: {"lines": [], "branches": [[229, 0]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = MagicMock()
    module._plugin_options = {'show_per_host_start': True}
    return module

def test_v2_runner_on_start(callback_module):
    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    callback_module._display.display.assert_called_once_with(f" [started {task} on {host}]", color=C.COLOR_OK)

def test_v2_runner_on_start_option_false(callback_module):
    callback_module._plugin_options['show_per_host_start'] = False
    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    callback_module._display.display.assert_not_called()
