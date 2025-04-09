# file: lib/ansible/executor/play_iterator.py:58-91
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 69], [68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 69], [68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}

import pytest
from ansible.executor.play_iterator import HostState

class PlayIterator:
    ITERATING_SETUP = 0
    ITERATING_TASKS = 1
    ITERATING_RESCUE = 2
    ITERATING_ALWAYS = 3
    ITERATING_COMPLETE = 4
    FAILED_NONE = 0
    FAILED_SETUP = 1
    FAILED_TASKS = 2
    FAILED_RESCUE = 4
    FAILED_ALWAYS = 8

@pytest.fixture
def host_state():
    blocks = [1, 2, 3]
    return HostState(blocks)

def test_host_state_str_all_states(host_state):
    host_state.cur_block = 1
    host_state.cur_regular_task = 2
    host_state.cur_rescue_task = 3
    host_state.cur_always_task = 4
    host_state.run_state = PlayIterator.ITERATING_TASKS
    host_state.fail_state = PlayIterator.FAILED_SETUP | PlayIterator.FAILED_TASKS
    host_state.pending_setup = True
    host_state.tasks_child_state = 'child_state_1'
    host_state.rescue_child_state = 'child_state_2'
    host_state.always_child_state = 'child_state_3'
    host_state.did_rescue = True
    host_state.did_start_at_task = True

    expected_str = ("HOST STATE: block=1, task=2, rescue=3, always=4, run_state=ITERATING_TASKS, "
                    "fail_state=FAILED_SETUP|FAILED_TASKS, pending_setup=True, tasks child state? (child_state_1), "
                    "rescue child state? (child_state_2), always child state? (child_state_3), did rescue? True, did start at task? True")
    assert str(host_state) == expected_str

def test_host_state_str_unknown_run_state(host_state):
    host_state.run_state = 10  # Invalid state to trigger "UNKNOWN STATE"
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=UNKNOWN STATE, "
                    "fail_state=FAILED_NONE, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_no_failures(host_state):
    host_state.fail_state = PlayIterator.FAILED_NONE
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, "
                    "fail_state=FAILED_NONE, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str

def test_host_state_str_multiple_failures(host_state):
    host_state.fail_state = PlayIterator.FAILED_SETUP | PlayIterator.FAILED_TASKS | PlayIterator.FAILED_RESCUE
    expected_str = ("HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, "
                    "fail_state=FAILED_SETUP|FAILED_TASKS|FAILED_RESCUE, pending_setup=False, tasks child state? (None), "
                    "rescue child state? (None), always child state? (None), did rescue? False, did start at task? False")
    assert str(host_state) == expected_str
