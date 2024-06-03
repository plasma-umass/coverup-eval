# file tornado/locks.py:228-233
# lines [228, 233]
# branches []

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_clear(event):
    # Set the internal flag to True first
    event._value = True
    assert event._value is True

    # Clear the event and check the internal flag
    event.clear()
    assert event._value is False
