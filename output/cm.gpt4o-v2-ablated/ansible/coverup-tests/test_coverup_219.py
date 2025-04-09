# file: lib/ansible/plugins/action/reboot.py:97-102
# asked: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}
# gained: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.task import Task
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=())
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    task = Task()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    action_module = ActionModule(task, connection, play_context, loader, variable_manager, None)
    return action_module

def test_check_delay_default(action_module):
    action_module._task.args = {}
    assert action_module._check_delay('delay', 10) == 10

def test_check_delay_key(action_module):
    action_module._task.args = {'delay': 5}
    assert action_module._check_delay('delay', 10) == 5

def test_check_delay_key_sec(action_module):
    action_module._task.args = {'delay_sec': 7}
    assert action_module._check_delay('delay', 10) == 7

def test_check_delay_negative(action_module):
    action_module._task.args = {'delay': -3}
    assert action_module._check_delay('delay', 10) == 0

def test_check_delay_key_sec_negative(action_module):
    action_module._task.args = {'delay_sec': -4}
    assert action_module._check_delay('delay', 10) == 0
