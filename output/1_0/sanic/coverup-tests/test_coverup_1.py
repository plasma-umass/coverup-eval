# file sanic/models/futures.py:33-35
# lines [33, 34, 35]
# branches []

import pytest
from sanic.models.futures import FutureMiddleware

@pytest.fixture
def future_middleware():
    return FutureMiddleware(middleware=lambda x: x, attach_to='request')

def test_future_middleware(future_middleware):
    assert future_middleware.middleware('test') == 'test'
    assert future_middleware.attach_to == 'request'
