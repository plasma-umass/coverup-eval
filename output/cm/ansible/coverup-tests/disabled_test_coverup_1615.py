# file lib/ansible/executor/play_iterator.py:511-520
# lines [516, 517, 518, 519, 520]
# branches ['516->517', '516->518', '518->519', '518->520']

import pytest
from ansible.executor.play_iterator import PlayIterator, HostState

# Assuming HostState and PlayIterator are defined in the module ansible.executor.play_iterator
# and that HostState has the attributes 'run_state' and 'tasks_child_state' as used in the method.
# Also assuming that the required arguments for PlayIterator and HostState can be mocked or created as needed.

@pytest.fixture
def play_iterator(mocker):
    inventory = mocker.MagicMock()
    play = mocker.MagicMock()
    play_context = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    all_vars = mocker.MagicMock()
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

@pytest.fixture
def host_state(mocker):
    blocks = mocker.MagicMock()
    return HostState(blocks)

def test_is_any_block_rescuing_with_rescue_state(play_iterator, host_state):
    host_state.run_state = PlayIterator.ITERATING_RESCUE
    assert play_iterator.is_any_block_rescuing(host_state) is True

def test_is_any_block_rescuing_with_child_state(play_iterator, host_state, mocker):
    mock_child_state = mocker.MagicMock()
    mock_child_state.run_state = PlayIterator.ITERATING_RESCUE
    host_state.tasks_child_state = mock_child_state
    assert play_iterator.is_any_block_rescuing(host_state) is True

def test_is_any_block_rescuing_without_rescue_state(play_iterator, host_state):
    host_state.run_state = None
    host_state.tasks_child_state = None
    assert play_iterator.is_any_block_rescuing(host_state) is False
