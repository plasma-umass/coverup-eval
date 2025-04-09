# file: lib/ansible/plugins/action/reboot.py:97-102
# asked: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}
# gained: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    return ActionModule(task, None, None, None, None, None)

def test_check_delay_default(action_module):
    action_module._task.args = {}
    assert action_module._check_delay('nonexistent_key', 10) == 10

def test_check_delay_key(action_module):
    action_module._task.args = {'test_key': 5}
    assert action_module._check_delay('test_key', 10) == 5

def test_check_delay_key_sec(action_module):
    action_module._task.args = {'test_key_sec': 7}
    assert action_module._check_delay('test_key', 10) == 7

def test_check_delay_negative(action_module):
    action_module._task.args = {'test_key': -5}
    assert action_module._check_delay('test_key', 10) == 0
