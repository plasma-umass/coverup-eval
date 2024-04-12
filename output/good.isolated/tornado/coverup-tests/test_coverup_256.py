# file tornado/locks.py:216-226
# lines [225, 226]
# branches ['221->exit', '224->225', '225->224', '225->226']

import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado import gen
from unittest.mock import Mock

@pytest.mark.gen_test
def test_event_set():
    event = Event()
    event._value = False  # Ensure the event is not set
    event._waiters = [Mock(done=lambda: False), Mock(done=lambda: True)]

    # Call set to trigger the branch we want to test
    event.set()

    # Check postconditions
    assert event._value is True
    event._waiters[0].set_result.assert_called_once_with(None)
    event._waiters[1].set_result.assert_not_called()

    # Clean up
    event._waiters.clear()
