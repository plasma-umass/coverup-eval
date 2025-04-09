# file lib/ansible/executor/play_iterator.py:58-91
# lines [59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
# branches ['68->69', '68->71', '72->73', '72->75', '73->72', '73->74']

import pytest

# Assuming the HostState class is part of a module named ansible.executor.play_iterator
from ansible.executor.play_iterator import HostState

# Mock the HostState attributes for testing
@pytest.fixture
def mock_host_state(mocker):
    # Assuming that the HostState class requires a 'blocks' argument for initialization
    # and that it is a list or similar iterable. We'll pass an empty list for this test.
    blocks = []
    host_state = HostState(blocks)
    mocker.patch.object(host_state, 'cur_block', 0)
    mocker.patch.object(host_state, 'cur_regular_task', 0)
    mocker.patch.object(host_state, 'cur_rescue_task', 0)
    mocker.patch.object(host_state, 'cur_always_task', 0)
    mocker.patch.object(host_state, 'run_state', 0)
    mocker.patch.object(host_state, 'fail_state', 0)
    mocker.patch.object(host_state, 'pending_setup', False)
    mocker.patch.object(host_state, 'tasks_child_state', None)
    mocker.patch.object(host_state, 'rescue_child_state', None)
    mocker.patch.object(host_state, 'always_child_state', None)
    mocker.patch.object(host_state, 'did_rescue', False)
    mocker.patch.object(host_state, 'did_start_at_task', False)
    return host_state

# Test function to cover lines 59-90
def test_host_state_str(mock_host_state):
    # Test with initial values
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, fail_state=FAILED_NONE, "
                    "pending_setup=False, tasks child state? (None), rescue child state? (None), always child state? (None), "
                    "did rescue? False, did start at task? False")
    assert str(mock_host_state) == expected_str

    # Test with different run_state and fail_state
    mock_host_state.run_state = 4  # ITERATING_COMPLETE
    mock_host_state.fail_state = 3  # FAILED_SETUP | FAILED_TASKS
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_COMPLETE, fail_state=FAILED_SETUP|FAILED_TASKS, "
                    "pending_setup=False, tasks child state? (None), rescue child state? (None), always child state? (None), "
                    "did rescue? False, did start at task? False")
    assert str(mock_host_state) == expected_str

    # Test with out-of-range run_state and fail_state
    mock_host_state.run_state = 99  # UNKNOWN STATE
    mock_host_state.fail_state = 16  # No matching state
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=UNKNOWN STATE, fail_state=, "
                    "pending_setup=False, tasks child state? (None), rescue child state? (None), always child state? (None), "
                    "did rescue? False, did start at task? False")
    assert str(mock_host_state) == expected_str
