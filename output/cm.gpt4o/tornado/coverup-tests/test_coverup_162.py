# file tornado/concurrent.py:52-53
# lines [52, 53]
# branches []

import pytest
from unittest.mock import Mock

# Assuming FUTURES is defined somewhere in tornado.concurrent
from tornado.concurrent import is_future

class MockFuture:
    pass

@pytest.fixture
def mock_future_class(mocker):
    mocker.patch('tornado.concurrent.FUTURES', (MockFuture,))
    yield
    mocker.stopall()

def test_is_future_with_future_instance(mock_future_class):
    future_instance = MockFuture()
    assert is_future(future_instance) == True

def test_is_future_with_non_future_instance(mock_future_class):
    non_future_instance = object()
    assert is_future(non_future_instance) == False
