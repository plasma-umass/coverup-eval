# file: lib/ansible/plugins/action/reboot.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.template import Templar

class MockActionBase:
    DEFAULT_PRE_REBOOT_DELAY = 10

    def _check_delay(self, delay_type, default_delay):
        if delay_type == 'pre_reboot_delay':
            return default_delay
        return 0

@pytest.fixture
def action_module(monkeypatch):
    # Mock the ActionBase class to avoid state pollution
    monkeypatch.setattr(ActionModule, 'DEFAULT_PRE_REBOOT_DELAY', MockActionBase.DEFAULT_PRE_REBOOT_DELAY)
    monkeypatch.setattr(ActionModule, '_check_delay', MockActionBase._check_delay)

    task = Task()
    connection = None
    play_context = PlayContext()
    loader = None
    templar = Templar(loader=loader)
    shared_loader_obj = None

    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_pre_reboot_delay_property(action_module):
    assert action_module.pre_reboot_delay == MockActionBase.DEFAULT_PRE_REBOOT_DELAY
