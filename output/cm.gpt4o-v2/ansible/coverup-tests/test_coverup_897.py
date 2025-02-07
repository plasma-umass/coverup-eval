# file: lib/ansible/plugins/action/reboot.py:86-87
# asked: {"lines": [86, 87], "branches": []}
# gained: {"lines": [86, 87], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

def test_action_module_init(monkeypatch):
    # Mock the __init__ method of ActionBase to ensure it is called
    def mock_init(self, *args, **kwargs):
        self.init_called = True

    monkeypatch.setattr(ActionBase, '__init__', mock_init)

    # Create an instance of ActionModule
    action_module = ActionModule()

    # Assert that the __init__ method of ActionBase was called
    assert hasattr(action_module, 'init_called')
    assert action_module.init_called
