# file: lib/ansible/executor/play_iterator.py:39-53
# asked: {"lines": [39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest

# Assuming the HostState class is defined within the PlayIterator module
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

class TestHostState:
    @pytest.fixture
    def mock_blocks(self):
        return ['block1', 'block2']

    def test_host_state_initialization(self, mock_blocks):
        host_state = HostState(mock_blocks)
        
        assert host_state._blocks == mock_blocks
        assert host_state.cur_block == 0
        assert host_state.cur_regular_task == 0
        assert host_state.cur_rescue_task == 0
        assert host_state.cur_always_task == 0
        assert host_state.run_state == PlayIterator.ITERATING_SETUP
        assert host_state.fail_state == PlayIterator.FAILED_NONE
        assert host_state.pending_setup is False
        assert host_state.tasks_child_state is None
        assert host_state.rescue_child_state is None
        assert host_state.always_child_state is None
        assert host_state.did_rescue is False
        assert host_state.did_start_at_task is False
