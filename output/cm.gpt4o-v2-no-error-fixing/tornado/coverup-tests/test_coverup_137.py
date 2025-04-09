# file: tornado/locks.py:157-159
# asked: {"lines": [157, 159], "branches": []}
# gained: {"lines": [157], "branches": []}

import pytest
from tornado.ioloop import IOLoop
from tornado.locks import Condition

@pytest.mark.gen_test
async def test_condition_notify_all():
    condition = Condition()
    waiter_notified = False

    async def waiter():
        nonlocal waiter_notified
        await condition.wait()
        waiter_notified = True

    async def notifier():
        await condition.notify_all()

    await IOLoop.current().run_in_executor(None, lambda: IOLoop.current().add_callback(waiter))
    await IOLoop.current().run_in_executor(None, lambda: IOLoop.current().add_callback(notifier))

    await IOLoop.current().run_in_executor(None, lambda: IOLoop.current().add_callback(lambda: None))  # Yield control to allow callbacks to run

    assert waiter_notified
