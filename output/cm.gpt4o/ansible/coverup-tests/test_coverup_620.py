# file lib/ansible/plugins/callback/minimal.py:22-32
# lines [22, 24, 29, 30, 31]
# branches []

import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.plugins.callback import CallbackBase

def test_callback_module_initialization():
    # Test that the CallbackModule can be initialized correctly
    callback = CallbackModule()
    assert isinstance(callback, CallbackBase)
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_NAME == 'minimal'
