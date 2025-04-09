# file tornado/locks.py:216-226
# lines []
# branches ['221->exit', '225->224']

import pytest
from tornado.locks import Event
from tornado.concurrent import Future

@pytest.fixture
def event():
    return Event()

def test_event_set(event, mocker):
    # Mock the _value attribute to ensure the branch is taken
    event._value = False

    # Create a mock future and add it to the _waiters list
    mock_future_done = mocker.Mock(spec=Future)
    mock_future_done.done.return_value = True

    mock_future_not_done = mocker.Mock(spec=Future)
    mock_future_not_done.done.return_value = False

    event._waiters = [mock_future_done, mock_future_not_done]

    # Call the set method
    event.set()

    # Assert that the _value attribute is set to True
    assert event._value is True

    # Assert that set_result was called on the mock future that was not done
    mock_future_not_done.set_result.assert_called_once_with(None)

    # Assert that set_result was not called on the mock future that was done
    mock_future_done.set_result.assert_not_called()

    # Clean up
    event._waiters = []
