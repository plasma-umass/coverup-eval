# file: lib/ansible/executor/play_iterator.py:108-125
# asked: {"lines": [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125], "branches": [[119, 120], [119, 121], [121, 122], [121, 123], [123, 124], [123, 125]]}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125], "branches": [[119, 120], [119, 121], [121, 122], [121, 123], [123, 124], [123, 125]]}

import pytest
from ansible.executor.play_iterator import HostState

def test_host_state_copy():
    # Initial setup
    original_state = HostState(blocks=[1, 2, 3])
    original_state.cur_block = 1
    original_state.cur_regular_task = 2
    original_state.cur_rescue_task = 3
    original_state.cur_always_task = 4
    original_state.run_state = "RUNNING"
    original_state.fail_state = "FAILED"
    original_state.pending_setup = True
    original_state.did_rescue = True
    original_state.did_start_at_task = True

    # Child states
    original_state.tasks_child_state = HostState(blocks=[4, 5, 6])
    original_state.rescue_child_state = HostState(blocks=[7, 8, 9])
    original_state.always_child_state = HostState(blocks=[10, 11, 12])

    # Perform the copy
    copied_state = original_state.copy()

    # Assertions to verify the copy
    assert copied_state._blocks == original_state._blocks
    assert copied_state.cur_block == original_state.cur_block
    assert copied_state.cur_regular_task == original_state.cur_regular_task
    assert copied_state.cur_rescue_task == original_state.cur_rescue_task
    assert copied_state.cur_always_task == original_state.cur_always_task
    assert copied_state.run_state == original_state.run_state
    assert copied_state.fail_state == original_state.fail_state
    assert copied_state.pending_setup == original_state.pending_setup
    assert copied_state.did_rescue == original_state.did_rescue
    assert copied_state.did_start_at_task == original_state.did_start_at_task

    # Assertions for child states
    assert copied_state.tasks_child_state._blocks == original_state.tasks_child_state._blocks
    assert copied_state.rescue_child_state._blocks == original_state.rescue_child_state._blocks
    assert copied_state.always_child_state._blocks == original_state.always_child_state._blocks

    # Ensure that the copied child states are not the same instances as the original ones
    assert copied_state.tasks_child_state is not original_state.tasks_child_state
    assert copied_state.rescue_child_state is not original_state.rescue_child_state
    assert copied_state.always_child_state is not original_state.always_child_state
