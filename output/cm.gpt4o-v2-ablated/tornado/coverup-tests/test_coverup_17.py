# file: tornado/locks.py:123-143
# asked: {"lines": [123, 124, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 143], "branches": [[133, 135], [133, 143], [136, 137], [136, 138]]}
# gained: {"lines": [123, 124], "branches": []}

import pytest
from tornado import ioloop
from tornado.concurrent import Future
from tornado.locks import Condition
from unittest.mock import MagicMock
import datetime

@pytest.fixture
def condition():
    return Condition()

@pytest.mark.asyncio
async def test_wait_no_timeout(condition):
    future = condition.wait()
    assert isinstance(future, Future)
    assert not future.done()
    condition.notify()
    await future
    assert future.done()
    assert future.result() is True

@pytest.mark.asyncio
async def test_wait_with_timeout(condition, monkeypatch):
    future = condition.wait(timeout=0.1)
    assert isinstance(future, Future)
    assert not future.done()

    io_loop = ioloop.IOLoop.current()
    mock_add_timeout = MagicMock()
    monkeypatch.setattr(io_loop, 'add_timeout', mock_add_timeout)
    mock_remove_timeout = MagicMock()
    monkeypatch.setattr(io_loop, 'remove_timeout', mock_remove_timeout)

    await future
    assert future.done()
    assert future.result() is False

    mock_add_timeout.assert_called_once()
    mock_remove_timeout.assert_called_once()

@pytest.mark.asyncio
async def test_wait_with_datetime_timeout(condition, monkeypatch):
    timeout = datetime.timedelta(seconds=0.1)
    future = condition.wait(timeout=timeout)
    assert isinstance(future, Future)
    assert not future.done()

    io_loop = ioloop.IOLoop.current()
    mock_add_timeout = MagicMock()
    monkeypatch.setattr(io_loop, 'add_timeout', mock_add_timeout)
    mock_remove_timeout = MagicMock()
    monkeypatch.setattr(io_loop, 'remove_timeout', mock_remove_timeout)

    await future
    assert future.done()
    assert future.result() is False

    mock_add_timeout.assert_called_once()
    mock_remove_timeout.assert_called_once()
