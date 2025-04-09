# file: lib/ansible/executor/play_iterator.py:105-106
# asked: {"lines": [105, 106], "branches": []}
# gained: {"lines": [105, 106], "branches": []}

import pytest
from ansible.executor.play_iterator import HostState

def test_get_current_block():
    blocks = ['block1', 'block2', 'block3']
    host_state = HostState(blocks)
    
    # Test initial state
    assert host_state.get_current_block() == 'block1'
    
    # Change state and test again
    host_state.cur_block = 1
    assert host_state.get_current_block() == 'block2'
    
    # Change state and test again
    host_state.cur_block = 2
    assert host_state.get_current_block() == 'block3'
    
    # Clean up
    del host_state
