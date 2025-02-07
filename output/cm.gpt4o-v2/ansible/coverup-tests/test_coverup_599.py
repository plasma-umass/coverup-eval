# file: lib/ansible/plugins/callback/default.py:56-62
# asked: {"lines": [56, 58, 59, 60, 61, 62], "branches": []}
# gained: {"lines": [56, 58, 59, 60, 61, 62], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_callback_module_initialization(callback_module):
    assert callback_module._play is None
    assert callback_module._last_task_banner is None
    assert callback_module._last_task_name is None
    assert callback_module._task_type_cache == {}
    assert hasattr(callback_module, '_display')
    assert hasattr(callback_module, 'disabled')
    assert hasattr(callback_module, 'wants_implicit_tasks')
    assert hasattr(callback_module, '_plugin_options')
    assert hasattr(callback_module, '_hide_in_debug')
