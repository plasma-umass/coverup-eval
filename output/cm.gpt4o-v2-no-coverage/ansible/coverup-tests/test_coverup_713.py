# file: lib/ansible/plugins/callback/default.py:228-230
# asked: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}
# gained: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = Mock()
    return module

def test_v2_runner_on_start_with_show_per_host_start(callback_module):
    callback_module.get_option = Mock(return_value=True)
    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    callback_module._display.display.assert_called_once_with(f" [started {task} on {host}]", color=C.COLOR_OK)

def test_v2_runner_on_start_without_show_per_host_start(callback_module):
    callback_module.get_option = Mock(return_value=False)
    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    callback_module._display.display.assert_not_called()
