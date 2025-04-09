# file lib/ansible/executor/play_iterator.py:93-103
# lines [94, 95, 97, 100, 101, 103]
# branches ['94->95', '94->97', '97->100', '97->103', '100->97', '100->101']

import pytest
from ansible.executor.play_iterator import HostState

def test_hoststate_equality():
    # Create two HostState instances with identical attributes
    hs1 = HostState(blocks=[])
    hs2 = HostState(blocks=[])
    
    # Set attributes to be identical
    for attr in ('_blocks', 'cur_block', 'cur_regular_task', 'cur_rescue_task', 'cur_always_task',
                 'run_state', 'fail_state', 'pending_setup',
                 'tasks_child_state', 'rescue_child_state', 'always_child_state'):
        setattr(hs1, attr, 'test_value')
        setattr(hs2, attr, 'test_value')
    
    # Test equality
    assert hs1 == hs2

    # Modify one attribute in hs2
    hs2.cur_block = 'different_value'
    
    # Test inequality
    assert hs1 != hs2

    # Test with an instance of a different class
    class DifferentClass:
        pass

    assert hs1 != DifferentClass()

    # Clean up by deleting the attributes
    for attr in ('_blocks', 'cur_block', 'cur_regular_task', 'cur_rescue_task', 'cur_always_task',
                 'run_state', 'fail_state', 'pending_setup',
                 'tasks_child_state', 'rescue_child_state', 'always_child_state'):
        delattr(hs1, attr)
        delattr(hs2, attr)
