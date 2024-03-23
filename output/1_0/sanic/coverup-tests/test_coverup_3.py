# file sanic/models/futures.py:28-30
# lines [28, 29, 30]
# branches []

import pytest
from sanic.models.futures import FutureListener

@pytest.fixture
def future_listener():
    return FutureListener(listener=lambda x: x, event="test_event")

def test_future_listener(future_listener):
    assert future_listener.listener("test") == "test", "Listener should return 'test'"
    assert future_listener.event == "test_event", "Event should be 'test_event'"
