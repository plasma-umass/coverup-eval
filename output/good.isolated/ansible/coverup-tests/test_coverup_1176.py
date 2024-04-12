# file lib/ansible/executor/play_iterator.py:108-125
# lines [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]
# branches ['119->120', '119->121', '121->122', '121->123', '123->124', '123->125']

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    state = HostState([])
    state.cur_block = None
    state.cur_regular_task = None
    state.cur_rescue_task = None
    state.cur_always_task = None
    state.run_state = None
    state.fail_state = None
    state.pending_setup = None
    state.did_rescue = None
    state.did_start_at_task = None
    state.tasks_child_state = None
    state.rescue_child_state = None
    state.always_child_state = None
    return state

def test_host_state_copy(host_state):
    # Set up child states to ensure lines 119-124 are covered
    host_state.tasks_child_state = HostState([])
    host_state.rescue_child_state = HostState([])
    host_state.always_child_state = HostState([])

    # Perform the copy
    new_state = host_state.copy()

    # Assertions to check if the copy was correct
    assert new_state.cur_block is host_state.cur_block
    assert new_state.cur_regular_task is host_state.cur_regular_task
    assert new_state.cur_rescue_task is host_state.cur_rescue_task
    assert new_state.cur_always_task is host_state.cur_always_task
    assert new_state.run_state is host_state.run_state
    assert new_state.fail_state is host_state.fail_state
    assert new_state.pending_setup is host_state.pending_setup
    assert new_state.did_rescue is host_state.did_rescue
    assert new_state.did_start_at_task is host_state.did_start_at_task
    assert new_state.tasks_child_state is not host_state.tasks_child_state
    assert new_state.rescue_child_state is not host_state.rescue_child_state
    assert new_state.always_child_state is not host_state.always_child_state
