# file lib/ansible/executor/play_iterator.py:495-497
# lines [496, 497]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the PlayIterator class is imported from ansible.executor.play_iterator
from ansible.executor.play_iterator import PlayIterator

@pytest.fixture
def play_iterator(mocker):
    # Mocking the required arguments for PlayIterator
    inventory = mocker.MagicMock()
    play = mocker.MagicMock()
    play_context = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    all_vars = mocker.MagicMock()
    
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_is_failed(play_iterator, mocker):
    host = 'test_host'
    mock_state = 'failed_state'
    
    # Mocking get_host_state to return a specific state
    mocker.patch.object(play_iterator, 'get_host_state', return_value=mock_state)
    
    # Mocking _check_failed_state to return True when called with mock_state
    mocker.patch.object(play_iterator, '_check_failed_state', return_value=True)
    
    # Call the method and assert the expected result
    result = play_iterator.is_failed(host)
    assert result == True
    
    # Verify that get_host_state and _check_failed_state were called with the correct arguments
    play_iterator.get_host_state.assert_called_once_with(host)
    play_iterator._check_failed_state.assert_called_once_with(mock_state)
