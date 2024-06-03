# file lib/ansible/executor/play_iterator.py:39-53
# lines [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator

@pytest.fixture
def host_state():
    class HostState:
        def __init__(self, blocks):
            self._blocks = blocks[:]
            self.cur_block = 0
            self.cur_regular_task = 0
            self.cur_rescue_task = 0
            self.cur_always_task = 0
            self.run_state = PlayIterator.ITERATING_SETUP
            self.fail_state = PlayIterator.FAILED_NONE
            self.pending_setup = False
            self.tasks_child_state = None
            self.rescue_child_state = None
            self.always_child_state = None
            self.did_rescue = False
            self.did_start_at_task = False

    return HostState

def test_host_state_initialization(host_state):
    blocks = ['block1', 'block2']
    state = host_state(blocks)

    assert state._blocks == blocks
    assert state.cur_block == 0
    assert state.cur_regular_task == 0
    assert state.cur_rescue_task == 0
    assert state.cur_always_task == 0
    assert state.run_state == PlayIterator.ITERATING_SETUP
    assert state.fail_state == PlayIterator.FAILED_NONE
    assert state.pending_setup is False
    assert state.tasks_child_state is None
    assert state.rescue_child_state is None
    assert state.always_child_state is None
    assert state.did_rescue is False
    assert state.did_start_at_task is False
