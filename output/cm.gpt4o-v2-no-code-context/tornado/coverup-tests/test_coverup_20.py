# file: tornado/locks.py:123-143
# asked: {"lines": [123, 124, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 143], "branches": [[133, 135], [133, 143], [136, 137], [136, 138]]}
# gained: {"lines": [123, 124], "branches": []}

import pytest
from tornado import ioloop
from tornado.concurrent import Future
from tornado.locks import Condition
from datetime import timedelta

@pytest.mark.asyncio
async def test_condition_wait_no_timeout():
    condition = Condition()
    future = condition.wait()
    assert isinstance(future, Future)
    assert not future.done()
    condition.notify()
    await future
    assert future.done()
    assert future.result() is True

@pytest.mark.asyncio
async def test_condition_wait_with_timeout():
    condition = Condition()
    timeout = timedelta(seconds=0.1)
    future = condition.wait(timeout=timeout)
    assert isinstance(future, Future)
    assert not future.done()
    await future
    assert future.done()
    assert future.result() is False

@pytest.mark.asyncio
async def test_condition_wait_with_timeout_and_notify():
    condition = Condition()
    timeout = timedelta(seconds=0.1)
    future = condition.wait(timeout=timeout)
    assert isinstance(future, Future)
    assert not future.done()
    ioloop.IOLoop.current().call_later(0.05, condition.notify)
    await future
    assert future.done()
    assert future.result() is True
