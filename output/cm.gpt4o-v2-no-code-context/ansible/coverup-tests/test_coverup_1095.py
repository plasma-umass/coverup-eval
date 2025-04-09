# file: lib/ansible/plugins/action/reboot.py:93-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

class MockActionBase:
    DEFAULT_POST_REBOOT_DELAY = 10

    def _check_delay(self, delay_type, default_delay):
        if delay_type == 'post_reboot_delay':
            return default_delay
        return None

@pytest.fixture
def action_module(monkeypatch):
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    monkeypatch.setattr(action_module, '_check_delay', MockActionBase()._check_delay)
    monkeypatch.setattr(action_module, 'DEFAULT_POST_REBOOT_DELAY', MockActionBase.DEFAULT_POST_REBOOT_DELAY)
    return action_module

def test_post_reboot_delay(action_module):
    assert action_module.post_reboot_delay == 10
