# file lib/ansible/plugins/callback/default.py:56-62
# lines [56, 58, 59, 60, 61, 62]
# branches []

import pytest
from ansible.plugins.callback import default

# Assuming the CallbackModule is part of a larger file, we would need to mock
# the dependencies and ensure the test is isolated.

def test_callback_module_initialization(mocker):
    mocker.patch('ansible.plugins.callback.default.CallbackBase.__init__')
    
    callback_module = default.CallbackModule()
    
    assert callback_module._play is None
    assert callback_module._last_task_banner is None
    assert callback_module._last_task_name is None
    assert callback_module._task_type_cache == {}
    default.CallbackBase.__init__.assert_called_once()
