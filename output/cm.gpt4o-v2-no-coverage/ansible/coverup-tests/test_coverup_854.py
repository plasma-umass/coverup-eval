# file: lib/ansible/executor/play_iterator.py:105-106
# asked: {"lines": [105, 106], "branches": []}
# gained: {"lines": [105, 106], "branches": []}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    blocks = ['block1', 'block2', 'block3']
    return HostState(blocks)

def test_get_current_block(host_state):
    assert host_state.get_current_block() == 'block1'
    host_state.cur_block = 1
    assert host_state.get_current_block() == 'block2'
    host_state.cur_block = 2
    assert host_state.get_current_block() == 'block3'
