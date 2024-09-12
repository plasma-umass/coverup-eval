# file: lib/ansible/executor/play_iterator.py:58-91
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 69], [68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 69], [68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}

import pytest
from ansible.executor.play_iterator import HostState, PlayIterator

@pytest.fixture
def host_state():
    blocks = [1, 2, 3]  # Example blocks
    return HostState(blocks)

def test_host_state_str_iterating_setup(host_state):
    host_state.run_state = PlayIterator.ITERATING_SETUP
    host_state.fail_state = PlayIterator.FAILED_NONE
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, fail_state=FAILED_NONE, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_iterating_tasks(host_state):
    host_state.run_state = PlayIterator.ITERATING_TASKS
    host_state.fail_state = PlayIterator.FAILED_TASKS
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_TASKS, fail_state=FAILED_TASKS, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_failed_multiple_states(host_state):
    host_state.run_state = PlayIterator.ITERATING_RESCUE
    host_state.fail_state = PlayIterator.FAILED_SETUP | PlayIterator.FAILED_TASKS
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_RESCUE, fail_state=FAILED_SETUP|FAILED_TASKS, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_unknown_run_state(host_state):
    host_state.run_state = 10  # Invalid state
    host_state.fail_state = 0
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=UNKNOWN STATE, fail_state=FAILED_NONE, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_unknown_fail_state(host_state):
    host_state.run_state = 0
    host_state.fail_state = 16  # Invalid state
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, fail_state=, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str
