# file lib/ansible/executor/play_iterator.py:462-468
# lines [463, 464, 465, 466, 467, 468]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.play import Play
from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play_context import PlayContext
from ansible.vars.manager import VariableManager
from ansible.utils.display import Display

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

# Test function to cover lines 463-468
def test_mark_host_failed(mock_display):
    # Setup
    inventory = InventoryManager(loader=None, sources='localhost,')
    play_context = PlayContext()
    variable_manager = VariableManager(loader=None, inventory=inventory)
    all_vars = dict()

    play = Play()
    host = inventory.get_host('localhost')
    iterator = PlayIterator(inventory=inventory, play_context=play_context, play=play, variable_manager=variable_manager, all_vars=all_vars)

    # Ensure the host is not already marked as failed
    assert host.name not in iterator._play._removed_hosts

    # Call the method to test
    iterator.mark_host_failed(host)

    # Assertions to verify postconditions
    assert host.name in iterator._play._removed_hosts
    assert iterator.get_host_state(host).fail_state

    # Cleanup is not necessary as we are not modifying any persistent state
