# file lib/ansible/executor/play_iterator.py:93-103
# lines [93, 94, 95, 97, 100, 101, 103]
# branches ['94->95', '94->97', '97->100', '97->103', '100->97', '100->101']

import pytest
from ansible.executor.play_iterator import HostState

# Test function to improve coverage for HostState __eq__ method
def test_host_state_equality():
    # Create a list to simulate the 'blocks' argument required by HostState
    blocks = []
    state1 = HostState(blocks)
    state2 = HostState(blocks)

    # Set attributes to both states to ensure they are equal
    attributes = ['cur_block', 'cur_regular_task', 'cur_rescue_task', 'cur_always_task',
                  'run_state', 'fail_state', 'pending_setup',
                  'tasks_child_state', 'rescue_child_state', 'always_child_state']
    for attr in attributes:
        setattr(state1, attr, None)
        setattr(state2, attr, None)

    # Assert that the states are equal
    assert state1 == state2

    # Change one attribute in state2 and assert they are not equal
    setattr(state2, 'cur_block', 1)
    assert state1 != state2

    # Test comparison with a different type
    assert state1 != object()

# Fixture to clean up after the test
@pytest.fixture(autouse=True)
def cleanup(request, mocker):
    # This is a placeholder for any cleanup logic if necessary
    # Currently, there is no persistent state to clean up after the test
    pass
