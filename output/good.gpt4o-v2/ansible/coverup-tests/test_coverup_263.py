# file: lib/ansible/executor/play_iterator.py:39-53
# asked: {"lines": [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}
# gained: {"lines": [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}

import pytest
from ansible.executor.play_iterator import PlayIterator, HostState

@pytest.fixture
def mock_blocks():
    return ['block1', 'block2', 'block3']

def test_host_state_initialization(mock_blocks):
    host_state = HostState(blocks=mock_blocks)
    
    assert host_state._blocks == mock_blocks
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert not host_state.pending_setup
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert not host_state.did_rescue
    assert not host_state.did_start_at_task
