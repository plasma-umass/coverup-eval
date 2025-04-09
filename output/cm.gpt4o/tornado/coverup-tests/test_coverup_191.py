# file tornado/locks.py:212-214
# lines [212, 214]
# branches []

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_is_set(event):
    # Initially, the event should not be set
    assert not event.is_set()

    # Set the event and check if it is set
    event.set()
    assert event.is_set()

    # Clear the event and check if it is not set
    event.clear()
    assert not event.is_set()
