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

def test_callback_module_super_init(mocker):
    mock_super_init = mocker.patch('ansible.plugins.callback.CallbackBase.__init__')
    callback_module = CallbackModule()
    mock_super_init.assert_called_once_with()
