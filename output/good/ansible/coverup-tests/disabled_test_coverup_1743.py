# file lib/ansible/executor/play_iterator.py:470-471
# lines [471]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator
from unittest.mock import MagicMock

# Test function to cover the missing line 471
def test_get_failed_hosts_with_failed_state():
    # Create mock objects for the required arguments of PlayIterator
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = MagicMock()

    # Setup the PlayIterator with mock arguments and a mock _host_states
    play_iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    play_iterator._host_states = {
        'host1': 'failed',
        'host2': 'ok',
        'host3': 'failed'
    }

    # Define a mock _check_failed_state method to return True for 'failed' state
    def mock_check_failed_state(state):
        return state == 'failed'

    # Replace the original _check_failed_state method with the mock
    play_iterator._check_failed_state = mock_check_failed_state

    # Call the method under test
    failed_hosts = play_iterator.get_failed_hosts()

    # Assertions to verify the postconditions
    assert failed_hosts == {'host1': True, 'host3': True}, "Failed hosts should only include hosts with a 'failed' state"

    # Cleanup is not necessary as we're using mock objects and a local instance of PlayIterator
