# file sanic/models/futures.py:12-25
# lines [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# branches []

import pytest
from sanic.models.futures import FutureRoute

@pytest.fixture
def future_route():
    return FutureRoute(
        handler="test_handler",
        uri="/test",
        methods=["GET"],
        host="localhost",
        strict_slashes=False,
        stream=False,
        version=1,
        name="test_route",
        ignore_body=False,
        websocket=False,
        subprotocols=None,
        unquote=False,
        static=False,
    )

def test_future_route_creation(future_route):
    assert future_route.handler == "test_handler"
    assert future_route.uri == "/test"
    assert future_route.methods == ["GET"]
    assert future_route.host == "localhost"
    assert future_route.strict_slashes is False
    assert future_route.stream is False
    assert future_route.version == 1
    assert future_route.name == "test_route"
    assert future_route.ignore_body is False
    assert future_route.websocket is False
    assert future_route.subprotocols is None
    assert future_route.unquote is False
    assert future_route.static is False
