# file lib/ansible/executor/play_iterator.py:236-254
# lines [238, 239, 241, 242, 243, 244, 246, 248, 249, 251, 252, 253, 254]
# branches ['242->243', '242->246', '248->249', '248->251']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the PlayIterator class and other necessary components are imported from ansible.executor.play_iterator
from ansible.executor.play_iterator import PlayIterator, display

@pytest.fixture
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = MagicMock()
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

@pytest.fixture
def host():
    host = MagicMock()
    host.name = "test_host"
    return host

def test_get_next_task_for_host_complete(play_iterator, host, mocker):
    mocker.patch.object(play_iterator, 'get_host_state', return_value=MagicMock(run_state=play_iterator.ITERATING_COMPLETE))
    mocker.patch.object(display, 'debug')

    state, task = play_iterator.get_next_task_for_host(host)

    play_iterator.get_host_state.assert_called_once_with(host)
    assert state.run_state == play_iterator.ITERATING_COMPLETE
    assert task is None
    display.debug.assert_any_call("host test_host is done iterating, returning")

def test_get_next_task_for_host_incomplete(play_iterator, host, mocker):
    mock_state = MagicMock(run_state="NOT_COMPLETE")
    mock_task = MagicMock()
    mocker.patch.object(play_iterator, 'get_host_state', return_value=mock_state)
    mocker.patch.object(play_iterator, '_get_next_task_from_state', return_value=(mock_state, mock_task))
    mocker.patch.object(display, 'debug')

    state, task = play_iterator.get_next_task_for_host(host)

    play_iterator.get_host_state.assert_called_once_with(host)
    play_iterator._get_next_task_from_state.assert_called_once_with(mock_state, host=host)
    assert state == mock_state
    assert task == mock_task
    display.debug.assert_any_call("getting the next task for host test_host")
    display.debug.assert_any_call("done getting next task for host test_host")
    display.debug.assert_any_call(" ^ task is: %s" % mock_task)
    display.debug.assert_any_call(" ^ state is: %s" % mock_state)
