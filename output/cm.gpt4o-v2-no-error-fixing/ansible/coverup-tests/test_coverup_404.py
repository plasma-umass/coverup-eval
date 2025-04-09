# file: lib/ansible/plugins/callback/default.py:56-62
# asked: {"lines": [56, 58, 59, 60, 61, 62], "branches": []}
# gained: {"lines": [56, 58, 59, 60, 61, 62], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule

def test_callback_module_init():
    # Create an instance of CallbackModule
    callback_module = CallbackModule()
    
    # Assertions to verify the postconditions
    assert callback_module._play is None
    assert callback_module._last_task_banner is None
    assert callback_module._last_task_name is None
    assert callback_module._task_type_cache == {}
