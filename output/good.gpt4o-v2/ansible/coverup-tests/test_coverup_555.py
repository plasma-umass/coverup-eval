# file: lib/ansible/plugins/action/reboot.py:97-102
# asked: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}
# gained: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = Mock()
    task.args = {}
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_delay_positive(action_module):
    action_module._task.args = {'delay': 10}
    result = action_module._check_delay('delay', 5)
    assert result == 10

def test_check_delay_default(action_module):
    action_module._task.args = {}
    result = action_module._check_delay('delay', 5)
    assert result == 5

def test_check_delay_negative(action_module):
    action_module._task.args = {'delay': -10}
    result = action_module._check_delay('delay', 5)
    assert result == 0

def test_check_delay_key_sec(action_module):
    action_module._task.args = {'delay_sec': 15}
    result = action_module._check_delay('delay', 5)
    assert result == 15
