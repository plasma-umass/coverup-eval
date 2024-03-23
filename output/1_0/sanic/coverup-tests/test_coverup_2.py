# file sanic/models/futures.py:56-59
# lines [56, 57, 58, 59]
# branches []

import pytest
from sanic.models.futures import FutureSignal

@pytest.fixture
def future_signal():
    return FutureSignal(handler=lambda x: x, event="test_event", condition={"key": "value"})

def test_future_signal(future_signal):
    assert future_signal.handler("test") == "test"
    assert future_signal.event == "test_event"
    assert future_signal.condition == {"key": "value"}
