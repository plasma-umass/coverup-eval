# file: lib/ansible/executor/play_iterator.py:522-524
# asked: {"lines": [522, 524], "branches": []}
# gained: {"lines": [522, 524], "branches": []}

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.play import Play
from ansible.playbook.play_context import PlayContext
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def play_iterator():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = {
        'name': "Test Play",
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [{'name': 'Test Task', 'debug': {'msg': 'Hello World'}}]
    }
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    play_context = PlayContext(play=play)
    return PlayIterator(inventory, play, play_context, variable_manager, {})

def test_get_original_task(play_iterator):
    host = "localhost"
    task = "dummy_task"
    
    original_task = play_iterator.get_original_task(host, task)
    
    assert original_task == (None, None)
