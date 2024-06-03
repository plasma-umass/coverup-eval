# file lib/ansible/executor/play_iterator.py:58-91
# lines [59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
# branches ['68->69', '68->71', '72->73', '72->75', '73->72', '73->74']

import pytest
from unittest.mock import Mock

# Assuming the HostState class is imported from ansible.executor.play_iterator
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    hs = HostState(blocks=[])
    hs.cur_block = 1
    hs.cur_regular_task = 2
    hs.cur_rescue_task = 3
    hs.cur_always_task = 4
    hs.run_state = 0
    hs.fail_state = 0
    hs.pending_setup = True
    hs.tasks_child_state = False
    hs.rescue_child_state = False
    hs.always_child_state = False
    hs.did_rescue = False
    hs.did_start_at_task = True
    return hs

def test_host_state_str_all_states(host_state):
    host_state.run_state = 4  # To cover _run_state_to_string
    host_state.fail_state = 15  # To cover _failed_state_to_string with multiple states

    result = str(host_state)
    assert "HOST STATE: block=1, task=2, rescue=3, always=4, run_state=ITERATING_COMPLETE, fail_state=FAILED_SETUP|FAILED_TASKS|FAILED_RESCUE|FAILED_ALWAYS, pending_setup=True, tasks child state? (False), rescue child state? (False), always child state? (False), did rescue? False, did start at task? True" in result

def test_host_state_str_unknown_run_state(host_state):
    host_state.run_state = 10  # To cover unknown state in _run_state_to_string

    result = str(host_state)
    assert "run_state=UNKNOWN STATE" in result

def test_host_state_str_failed_none(host_state):
    host_state.fail_state = 0  # To cover FAILED_NONE in _failed_state_to_string

    result = str(host_state)
    assert "fail_state=FAILED_NONE" in result

def test_host_state_str_single_failed_state(host_state):
    host_state.fail_state = 2  # To cover single state in _failed_state_to_string

    result = str(host_state)
    assert "fail_state=FAILED_TASKS" in result
