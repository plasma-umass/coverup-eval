# file: lib/ansible/executor/play_iterator.py:55-56
# asked: {"lines": [55, 56], "branches": []}
# gained: {"lines": [55, 56], "branches": []}

import pytest
from ansible.executor.play_iterator import HostState

def test_hoststate_repr():
    blocks = ['block1', 'block2']
    host_state = HostState(blocks)
    assert repr(host_state) == "HostState(['block1', 'block2'])"

