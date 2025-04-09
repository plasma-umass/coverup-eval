# file tornado/concurrent.py:209-230
# lines [209, 228, 229, 230]
# branches ['228->229', '228->230']

import pytest
from tornado.concurrent import future_set_exc_info
from concurrent.futures import Future

def test_future_set_exc_info_with_no_exception():
    future = Future()

    with pytest.raises(Exception) as exc_info:
        future_set_exc_info(future, (None, None, None))

    assert str(exc_info.value) == "future_set_exc_info called with no exception"

def test_future_set_exc_info_with_exception():
    future = Future()
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        exc_info = (type(e), e, e.__traceback__)

    future_set_exc_info(future, exc_info)
    assert future.exception() == exc_info[1]

def test_future_set_exc_info_with_cancelled_future(mocker):
    future = Future()
    future.cancel()
    mocker.spy(future, 'set_exception')

    try:
        raise ValueError("Test exception")
    except ValueError as e:
        exc_info = (type(e), e, e.__traceback__)

    future_set_exc_info(future, exc_info)
    future.set_exception.assert_not_called()
