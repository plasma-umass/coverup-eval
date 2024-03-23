# file lib/ansible/executor/play_iterator.py:221-228
# lines [225, 226, 228]
# branches ['225->226', '225->228']

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.block import Block
from ansible.playbook.play import Play
from ansible.inventory.host import Host
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play_context import PlayContext

class HostState:
    def __init__(self, blocks):
        self._blocks = blocks

    def copy(self):
        return HostState(blocks=self._blocks.copy())

@pytest.fixture
def play_iterator(mocker):
    mocker.patch('ansible.executor.play_iterator.HostState', HostState)
    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play = Play.load(dict(name="test", hosts='all'), variable_manager=variable_manager, loader=None)
    play_context = PlayContext(play=play)
    return PlayIterator(inventory=inventory, play=play, play_context=play_context, variable_manager=variable_manager, all_vars=dict())

def test_get_host_state_with_nonexistent_host(play_iterator):
    # Create a host that is not in the inventory
    fake_host = Host(name='fake_host')
    # Ensure the host is not in the _host_states
    assert fake_host.name not in play_iterator._host_states
    # Call get_host_state which should add the host to _host_states
    host_state = play_iterator.get_host_state(fake_host)
    # Verify that the host has been added with an empty blocks list
    assert fake_host.name in play_iterator._host_states
    assert isinstance(host_state, HostState)
    assert host_state._blocks == []
    # Cleanup: remove the fake host from _host_states to not affect other tests
    del play_iterator._host_states[fake_host.name]
