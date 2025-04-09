# file lib/ansible/executor/play_iterator.py:462-468
# lines [462, 463, 464, 465, 466, 467, 468]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

@pytest.fixture
def play_iterator():
    # Create a PlayIterator instance with the necessary mocks
    mock_play = MagicMock()
    mock_play_context = MagicMock()
    mock_variable_manager = MagicMock()
    mock_all_vars = MagicMock()
    mock_inventory = MagicMock()
    pi = PlayIterator(
        play=mock_play,
        play_context=mock_play_context,
        variable_manager=mock_variable_manager,
        all_vars=mock_all_vars,
        inventory=mock_inventory
    )
    pi._host_states = {}
    pi._play = MagicMock()
    pi._play._removed_hosts = []
    return pi

def test_mark_host_failed(mock_display, play_iterator):
    # Create a mock host
    mock_host = MagicMock()
    mock_host.name = 'test_host'

    # Ensure the host is not already marked as failed
    assert mock_host.name not in play_iterator._play._removed_hosts

    # Call the method to be tested
    play_iterator.mark_host_failed(mock_host)

    # Check that the host is now marked as failed
    assert mock_host.name in play_iterator._play._removed_hosts
    assert play_iterator._host_states[mock_host.name] is not None

    # Clean up after the test
    play_iterator._play._removed_hosts.remove(mock_host.name)
    del play_iterator._host_states[mock_host.name]
