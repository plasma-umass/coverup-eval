# file lib/ansible/executor/play_iterator.py:128-144
# lines [128, 131, 132, 133, 134, 135, 139, 140, 141, 142, 143]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator

def test_play_iterator_states():
    # Verify the primary running states
    assert PlayIterator.ITERATING_SETUP == 0
    assert PlayIterator.ITERATING_TASKS == 1
    assert PlayIterator.ITERATING_RESCUE == 2
    assert PlayIterator.ITERATING_ALWAYS == 3
    assert PlayIterator.ITERATING_COMPLETE == 4

    # Verify the failure states
    assert PlayIterator.FAILED_NONE == 0
    assert PlayIterator.FAILED_SETUP == 1
    assert PlayIterator.FAILED_TASKS == 2
    assert PlayIterator.FAILED_RESCUE == 4
    assert PlayIterator.FAILED_ALWAYS == 8

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code to ensure no side effects on other tests
    yield
    # Add any necessary cleanup code here

