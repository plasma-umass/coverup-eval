# file lib/ansible/executor/play_iterator.py:55-56
# lines [55, 56]
# branches []

import pytest
from ansible.executor.play_iterator import HostState

def test_host_state_repr(mocker):
    # Setup the HostState with a mock _blocks attribute
    mock_blocks = ['block1', 'block2']
    host_state = HostState(blocks=mock_blocks)

    # Test the __repr__ method
    expected_repr = "HostState(%r)" % mock_blocks
    assert repr(host_state) == expected_repr

    # No cleanup required as no persistent state is modified
