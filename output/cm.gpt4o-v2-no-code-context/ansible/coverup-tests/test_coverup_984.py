# file: lib/ansible/executor/play_iterator.py:93-103
# asked: {"lines": [94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}
# gained: {"lines": [94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}

import pytest
from ansible.executor.play_iterator import HostState

@pytest.fixture
def host_state():
    hs = HostState(blocks=[])
    hs.cur_block = None
    hs.cur_regular_task = None
    hs.cur_rescue_task = None
    hs.cur_always_task = None
    hs.run_state = None
    hs.fail_state = None
    hs.pending_setup = None
    hs.tasks_child_state = None
    hs.rescue_child_state = None
    hs.always_child_state = None
    return hs

def test_host_state_eq_same_instance(host_state):
    assert host_state == host_state

def test_host_state_eq_different_instance_same_values(host_state):
    other = HostState(blocks=[])
    other.cur_block = None
    other.cur_regular_task = None
    other.cur_rescue_task = None
    other.cur_always_task = None
    other.run_state = None
    other.fail_state = None
    other.pending_setup = None
    other.tasks_child_state = None
    other.rescue_child_state = None
    other.always_child_state = None
    assert host_state == other

def test_host_state_eq_different_instance_different_values(host_state):
    other = HostState(blocks=['different'])
    other.cur_block = None
    other.cur_regular_task = None
    other.cur_rescue_task = None
    other.cur_always_task = None
    other.run_state = None
    other.fail_state = None
    other.pending_setup = None
    other.tasks_child_state = None
    other.rescue_child_state = None
    other.always_child_state = None
    assert host_state != other

def test_host_state_eq_different_type(host_state):
    assert host_state != object()
