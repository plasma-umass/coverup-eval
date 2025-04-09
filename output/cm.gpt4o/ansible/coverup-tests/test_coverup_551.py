# file lib/ansible/plugins/action/reboot.py:97-102
# lines [97, 99, 100, 101, 102]
# branches ['100->101', '100->102']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_delay_positive(action_module):
    action_module._task.args = {'delay': 10}
    assert action_module._check_delay('delay', 5) == 10

def test_check_delay_default(action_module):
    action_module._task.args = {}
    assert action_module._check_delay('delay', 5) == 5

def test_check_delay_negative(action_module):
    action_module._task.args = {'delay': -10}
    assert action_module._check_delay('delay', 5) == 0

def test_check_delay_sec(action_module):
    action_module._task.args = {'delay_sec': 15}
    assert action_module._check_delay('delay', 5) == 15

def test_check_delay_sec_negative(action_module):
    action_module._task.args = {'delay_sec': -15}
    assert action_module._check_delay('delay', 5) == 0
