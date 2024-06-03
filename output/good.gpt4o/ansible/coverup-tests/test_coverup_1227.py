# file lib/ansible/plugins/callback/default.py:228-230
# lines [229, 230]
# branches ['229->exit', '229->230']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = Display()
    return module

def test_v2_runner_on_start_show_per_host_start(callback_module, mocker):
    mocker.patch.object(callback_module, 'get_option', return_value=True)
    mock_display = mocker.patch.object(callback_module._display, 'display')

    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    mock_display.assert_called_once_with(" [started %s on %s]" % (task, host), color=C.COLOR_OK)

def test_v2_runner_on_start_no_show_per_host_start(callback_module, mocker):
    mocker.patch.object(callback_module, 'get_option', return_value=False)
    mock_display = mocker.patch.object(callback_module._display, 'display')

    host = 'localhost'
    task = 'test_task'
    
    callback_module.v2_runner_on_start(host, task)
    
    mock_display.assert_not_called()
