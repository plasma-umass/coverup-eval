# file tornado/locks.py:228-233
# lines [228, 233]
# branches []

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_clear(event):
    # Initially, the event should not be set
    assert not event.is_set()
    
    # Set the event and ensure it's set
    event.set()
    assert event.is_set()
    
    # Clear the event and ensure it's cleared
    event.clear()
    assert not event.is_set()
