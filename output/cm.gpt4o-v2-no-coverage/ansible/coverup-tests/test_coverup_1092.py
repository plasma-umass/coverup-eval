# file: lib/ansible/executor/play_iterator.py:58-91
# asked: {"lines": [59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 69], [68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}
# gained: {"lines": [59, 60, 61, 62, 66, 67, 68, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[68, 71], [72, 73], [72, 75], [73, 72], [73, 74]]}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
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

    blocks = [1, 2, 3]
    hs = HostState(blocks)
    hs.cur_block = 1
    hs.cur_regular_task = 2
    hs.cur_rescue_task = 3
    hs.cur_always_task = 4
    hs.run_state = PlayIterator.ITERATING_TASKS
    hs.fail_state = PlayIterator.FAILED_TASKS | PlayIterator.FAILED_RESCUE
    hs.pending_setup = True
    hs.tasks_child_state = True
    hs.rescue_child_state = False
    hs.always_child_state = True
    hs.did_rescue = True
    hs.did_start_at_task = False
    return hs

def test_host_state_str(host_state):
    expected_str = ("HOST STATE: block=1, task=2, rescue=3, always=4, run_state=ITERATING_TASKS, fail_state=FAILED_TASKS|FAILED_RESCUE, pending_setup=True, tasks child state? (True), "
                    "rescue child state? (False), always child state? (True), did rescue? True, did start at task? False")
    assert str(host_state) == expected_str
