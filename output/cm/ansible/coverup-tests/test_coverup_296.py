# file lib/ansible/executor/play_iterator.py:39-53
# lines [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator, HostState

# Assuming the existence of the PlayIterator class with the constants used in HostState
# If these constants do not exist, they should be added to the PlayIterator class accordingly.

def test_host_state_initialization(mocker):
    # Setup
    mock_blocks = [mocker.MagicMock()]

    # Exercise
    host_state = HostState(mock_blocks)

    # Verify
    assert host_state._blocks == mock_blocks[:]
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert host_state.pending_setup is False
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert host_state.did_rescue is False
    assert host_state.did_start_at_task is False

    # Cleanup - nothing to clean up as no external resources were modified
