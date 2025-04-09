# file lib/ansible/executor/play_iterator.py:470-471
# lines [470, 471]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the PlayIterator class is part of the ansible.executor.play_iterator module
from ansible.executor.play_iterator import PlayIterator

@pytest.fixture
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = MagicMock()
    
    iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    iterator._host_states = {
        'host1': MagicMock(),
        'host2': MagicMock(),
        'host3': MagicMock()
    }
    iterator._check_failed_state = MagicMock(side_effect=lambda state: state.failed)
    return iterator

def test_get_failed_hosts(play_iterator):
    # Set up the mock states
    play_iterator._host_states['host1'].failed = True
    play_iterator._host_states['host2'].failed = False
    play_iterator._host_states['host3'].failed = True

    # Call the method
    failed_hosts = play_iterator.get_failed_hosts()

    # Assertions to verify the correct hosts are marked as failed
    assert failed_hosts == {
        'host1': True,
        'host3': True
    }

    # Clean up
    play_iterator._host_states.clear()
