# file: lib/ansible/plugins/action/reboot.py:97-102
# asked: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}
# gained: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def action_module():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    task = Task()
    connection = None
    templar = None
    shared_loader_obj = None
    action_module = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj
    )
    return action_module

def test_check_delay_positive_value(action_module):
    action_module._task.args = {'delay': 10}
    result = action_module._check_delay('delay', 5)
    assert result == 10

def test_check_delay_default_value(action_module):
    action_module._task.args = {}
    result = action_module._check_delay('delay', 5)
    assert result == 5

def test_check_delay_negative_value(action_module):
    action_module._task.args = {'delay': -10}
    result = action_module._check_delay('delay', 5)
    assert result == 0

def test_check_delay_alternate_key(action_module):
    action_module._task.args = {'delay_sec': 20}
    result = action_module._check_delay('delay', 5)
    assert result == 20
