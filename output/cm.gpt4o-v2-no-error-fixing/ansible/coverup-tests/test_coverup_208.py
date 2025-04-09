# file: lib/ansible/executor/play_iterator.py:93-103
# asked: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}
# gained: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    return HostState(blocks=[1, 2, 3])

def test_host_state_equality_same_object(host_state):
    other = host_state
    assert host_state == other

def test_host_state_equality_different_type(host_state):
    other = "not a HostState"
    assert not host_state == other

def test_host_state_equality_different_blocks(host_state):
    other = HostState(blocks=[4, 5, 6])
    assert not host_state == other

def test_host_state_equality_different_cur_block(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.cur_block = 1
    assert not host_state == other

def test_host_state_equality_different_cur_regular_task(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.cur_regular_task = 1
    assert not host_state == other

def test_host_state_equality_different_cur_rescue_task(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.cur_rescue_task = 1
    assert not host_state == other

def test_host_state_equality_different_cur_always_task(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.cur_always_task = 1
    assert not host_state == other

def test_host_state_equality_different_run_state(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.run_state = "different_state"
    assert not host_state == other

def test_host_state_equality_different_fail_state(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.fail_state = "different_state"
    assert not host_state == other

def test_host_state_equality_different_pending_setup(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.pending_setup = True
    assert not host_state == other

def test_host_state_equality_different_tasks_child_state(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.tasks_child_state = "different_state"
    assert not host_state == other

def test_host_state_equality_different_rescue_child_state(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.rescue_child_state = "different_state"
    assert not host_state == other

def test_host_state_equality_different_always_child_state(host_state):
    other = HostState(blocks=[1, 2, 3])
    other.always_child_state = "different_state"
    assert not host_state == other
