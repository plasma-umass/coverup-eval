# file lib/ansible/executor/play_iterator.py:495-497
# lines [495, 496, 497]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the PlayIterator class is defined in the module ansible.executor.play_iterator
from ansible.executor.play_iterator import PlayIterator

# Mock the PlayIterator to not require the full initialization parameters
class MockedPlayIterator(PlayIterator):
    def __init__(self):
        self._play_context = MagicMock()
        self._variable_manager = MagicMock()
        self._all_vars = MagicMock()
        self._inventory = MagicMock()
        self._host = MagicMock()

    def get_host_state(self, host):
        return self._host_state

    def _check_failed_state(self, state):
        return state.failed

# Define a simple state class to simulate host state
class HostState:
    def __init__(self, failed):
        self.failed = failed

@pytest.fixture
def play_iterator():
    return MockedPlayIterator()

def test_play_iterator_is_failed(play_iterator):
    # Simulate a host state that is not failed
    play_iterator._host_state = HostState(failed=False)
    assert not play_iterator.is_failed(play_iterator._host), "Host should not be marked as failed"

    # Simulate a host state that is failed
    play_iterator._host_state = HostState(failed=True)
    assert play_iterator.is_failed(play_iterator._host), "Host should be marked as failed"
