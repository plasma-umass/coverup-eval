# file: lib/ansible/executor/play_iterator.py:93-103
# asked: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}
# gained: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    return HostState(blocks=[1, 2, 3])

def test_host_state_equality_same_object(host_state):
    assert host_state == host_state

def test_host_state_equality_different_object_same_values():
    host_state1 = HostState(blocks=[1, 2, 3])
    host_state2 = HostState(blocks=[1, 2, 3])
    assert host_state1 == host_state2

def test_host_state_equality_different_object_different_values():
    host_state1 = HostState(blocks=[1, 2, 3])
    host_state2 = HostState(blocks=[4, 5, 6])
    assert host_state1 != host_state2

def test_host_state_equality_different_type():
    host_state = HostState(blocks=[1, 2, 3])
    assert host_state != "not a HostState"

def test_host_state_equality_different_attributes():
    host_state1 = HostState(blocks=[1, 2, 3])
    host_state2 = HostState(blocks=[1, 2, 3])
    host_state2.cur_block = 1
    assert host_state1 != host_state2
