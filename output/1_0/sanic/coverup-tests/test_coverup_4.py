# file sanic/models/futures.py:38-40
# lines [38, 39, 40]
# branches []

import pytest
from sanic.models.futures import FutureException
from sanic.handlers import ErrorHandler
from typing import List

# Assuming the ErrorMiddlewareType is a callable that takes a request and an exception
ErrorMiddlewareType = callable

@pytest.fixture
def error_middleware():
    async def middleware(request, exception):
        return "Error handled"
    return middleware

@pytest.fixture
def base_exceptions():
    return [Exception("Test Exception 1"), Exception("Test Exception 2")]

def test_future_exception(error_middleware, base_exceptions):
    future_exception = FutureException(handler=error_middleware, exceptions=base_exceptions)
    assert future_exception.handler == error_middleware
    assert future_exception.exceptions == base_exceptions
    assert isinstance(future_exception.exceptions, List)
    assert all(isinstance(exc, BaseException) for exc in future_exception.exceptions)
