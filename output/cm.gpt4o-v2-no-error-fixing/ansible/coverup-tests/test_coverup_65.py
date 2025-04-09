# file: lib/ansible/executor/play_iterator.py:108-125
# asked: {"lines": [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125], "branches": [[119, 120], [119, 121], [121, 122], [121, 123], [123, 124], [123, 125]]}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125], "branches": [[119, 120], [119, 121], [121, 122], [121, 123], [123, 124], [123, 125]]}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    state = HostState(blocks=[1, 2, 3])
    state.cur_block = 1
    state.cur_regular_task = 2
    state.cur_rescue_task = 3
    state.cur_always_task = 4
    state.run_state = 'running'
    state.fail_state = 'failed'
    state.pending_setup = True
    state.did_rescue = True
    state.did_start_at_task = True
    state.tasks_child_state = HostState(blocks=[4, 5, 6])
    state.rescue_child_state = HostState(blocks=[7, 8, 9])
    state.always_child_state = HostState(blocks=[10, 11, 12])
    return state

def test_copy_host_state(host_state):
    copied_state = host_state.copy()
    
    assert copied_state._blocks == host_state._blocks
    assert copied_state.cur_block == host_state.cur_block
    assert copied_state.cur_regular_task == host_state.cur_regular_task
    assert copied_state.cur_rescue_task == host_state.cur_rescue_task
    assert copied_state.cur_always_task == host_state.cur_always_task
    assert copied_state.run_state == host_state.run_state
    assert copied_state.fail_state == host_state.fail_state
    assert copied_state.pending_setup == host_state.pending_setup
    assert copied_state.did_rescue == host_state.did_rescue
    assert copied_state.did_start_at_task == host_state.did_start_at_task
    assert copied_state.tasks_child_state._blocks == host_state.tasks_child_state._blocks
    assert copied_state.rescue_child_state._blocks == host_state.rescue_child_state._blocks
    assert copied_state.always_child_state._blocks == host_state.always_child_state._blocks
