# file tornado/locks.py:206-210
# lines [206, 207, 208, 209]
# branches []

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_repr(event):
    # Test when the event is clear
    assert repr(event) == "<Event clear>"
    
    # Set the event and test again
    event.set()
    assert repr(event) == "<Event set>"

    # Clean up by clearing the event
    event.clear()
    assert repr(event) == "<Event clear>"
