# file: lib/ansible/executor/play_iterator.py:93-103
# asked: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}
# gained: {"lines": [93, 94, 95, 97, 100, 101, 103], "branches": [[94, 95], [94, 97], [97, 100], [97, 103], [100, 97], [100, 101]]}

import pytest
from ansible.executor.play_iterator import HostState

def test_hoststate_equality():
    # Create two identical HostState objects
    blocks = [1, 2, 3]
    hs1 = HostState(blocks)
    hs2 = HostState(blocks)
    
    # Ensure they are considered equal
    assert hs1 == hs2

    # Modify an attribute in hs2 and ensure they are not equal
    hs2.cur_block = 1
    assert hs1 != hs2

    # Modify an attribute in hs1 to match hs2 and ensure they are equal again
    hs1.cur_block = 1
    assert hs1 == hs2

    # Modify a different attribute in hs2 and ensure they are not equal
    hs2.cur_regular_task = 1
    assert hs1 != hs2

    # Modify an attribute in hs1 to match hs2 and ensure they are equal again
    hs1.cur_regular_task = 1
    assert hs1 == hs2

    # Modify a non-matching attribute in hs2 and ensure they are not equal
    hs2.run_state = 'different_state'
    assert hs1 != hs2

    # Modify an attribute in hs1 to match hs2 and ensure they are equal again
    hs1.run_state = 'different_state'
    assert hs1 == hs2

    # Ensure comparison with a non-HostState object returns False
    assert hs1 != "not_a_hoststate"

    # Ensure comparison with None returns False
    assert hs1 != None
