# file tornado/locks.py:53-102
# lines [53, 54]
# branches []

import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Condition
from datetime import timedelta

@pytest.mark.asyncio
async def test_condition_wait_notify():
    condition = Condition()
    notified = False

    async def waiter():
        nonlocal notified
        await condition.wait()
        notified = True

    async def notifier():
        await gen.sleep(0.1)
        condition.notify()

    await gen.multi([waiter(), notifier()])
    assert notified

@pytest.mark.asyncio
async def test_condition_wait_timeout_absolute(mocker):
    condition = Condition()
    io_loop = IOLoop.current()
    timeout = io_loop.time() + 0.1

    async def waiter():
        result = await condition.wait(timeout=timeout)
        return result

    result = await waiter()
    assert result is False

@pytest.mark.asyncio
async def test_condition_wait_timeout_relative(mocker):
    condition = Condition()
    timeout = timedelta(seconds=0.1)

    async def waiter():
        result = await condition.wait(timeout=timeout)
        return result

    result = await waiter()
    assert result is False
