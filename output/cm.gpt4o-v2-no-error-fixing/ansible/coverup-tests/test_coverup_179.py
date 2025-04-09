# file: lib/ansible/executor/play_iterator.py:39-53
# asked: {"lines": [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest
from ansible.executor.play_iterator import PlayIterator

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

def test_host_state_initialization():
    blocks = ['block1', 'block2']
    host_state = HostState(blocks)

    assert host_state._blocks == blocks
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
