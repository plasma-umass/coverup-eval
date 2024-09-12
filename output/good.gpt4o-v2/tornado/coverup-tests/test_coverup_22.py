# file: tornado/locks.py:123-143
# asked: {"lines": [123, 124, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 143], "branches": [[133, 135], [133, 143], [136, 137], [136, 138]]}
# gained: {"lines": [123, 124], "branches": []}

import pytest
import datetime
from tornado import ioloop
from tornado.locks import Condition

@pytest.mark.gen_test
async def test_condition_wait_no_timeout():
    condition = Condition()
    future = condition.wait()
    condition.notify()
    result = await future
    assert result is True

@pytest.mark.gen_test
async def test_condition_wait_with_timeout():
    condition = Condition()
    future = condition.wait(timeout=0.1)
    result = await future
    assert result is False

@pytest.mark.gen_test
async def test_condition_wait_with_timedelta_timeout():
    condition = Condition()
    future = condition.wait(timeout=datetime.timedelta(seconds=0.1))
    result = await future
    assert result is False

@pytest.mark.gen_test
async def test_condition_wait_timeout_cancellation(mocker):
    condition = Condition()
    future = condition.wait(timeout=0.1)
    mocker.patch.object(future, 'done', return_value=True)
    result = await future
    assert result is False
