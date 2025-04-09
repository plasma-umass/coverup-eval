# file: tornado/locks.py:123-143
# asked: {"lines": [123, 124, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 143], "branches": [[133, 135], [133, 143], [136, 137], [136, 138]]}
# gained: {"lines": [123, 124], "branches": []}

import pytest
import datetime
from tornado import ioloop
from tornado.locks import Condition
from tornado.concurrent import Future

@pytest.mark.gen_test
async def test_condition_wait_no_timeout():
    condition = Condition()
    future = condition.wait()
    assert isinstance(future, Future)
    condition.notify()
    result = await future
    assert result is True

@pytest.mark.gen_test
async def test_condition_wait_with_timeout():
    condition = Condition()
    timeout = datetime.timedelta(seconds=1)
    future = condition.wait(timeout=timeout)
    assert isinstance(future, Future)
    result = await future
    assert result is False

@pytest.mark.gen_test
async def test_condition_wait_with_timeout_and_notify():
    condition = Condition()
    timeout = datetime.timedelta(seconds=1)
    future = condition.wait(timeout=timeout)
    assert isinstance(future, Future)
    condition.notify()
    result = await future
    assert result is True
