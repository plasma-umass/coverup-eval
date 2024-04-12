# file lib/ansible/executor/play_iterator.py:105-106
# lines [105, 106]
# branches []

import pytest
from ansible.executor.play_iterator import HostState

# Test function to cover get_current_block method
def test_get_current_block():
    # Setup the HostState with a mock block list and current block index
    mock_blocks = ['block1', 'block2', 'block3']
    host_state = HostState(blocks=mock_blocks)  # Pass the mock blocks to the constructor
    host_state.cur_block = 1  # Set current block index to 1

    # Call the method under test
    current_block = host_state.get_current_block()

    # Assert that the returned block is correct
    assert current_block == mock_blocks[1], "The current block returned is not correct"

    # Cleanup is not necessary as we are not modifying any external state or resources
