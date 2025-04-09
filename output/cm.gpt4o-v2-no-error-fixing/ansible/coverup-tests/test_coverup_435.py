# file: lib/ansible/plugins/callback/default.py:228-230
# asked: {"lines": [228, 229, 230], "branches": [[229, 0], [229, 230]]}
# gained: {"lines": [228, 229, 230], "branches": [[229, 230]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = MagicMock()
    module.get_option = MagicMock(return_value=True)
    return module

def test_v2_runner_on_start(callback_module):
    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    callback_module.get_option.assert_called_once_with('show_per_host_start')
    callback_module._display.display.assert_called_once_with(f" [started {task} on {host}]", color=C.COLOR_OK)
