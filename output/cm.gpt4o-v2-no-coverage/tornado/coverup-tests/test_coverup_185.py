# file: tornado/locks.py:117-121
# asked: {"lines": [118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}
# gained: {"lines": [118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}

import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop

@pytest.fixture
def condition():
    return Condition()

def test_condition_repr_no_waiters(condition):
    assert repr(condition) == "<Condition>"

def test_condition_repr_with_waiters(condition):
    condition._waiters.append(object())  # Simulate a waiter
    assert repr(condition) == "<Condition waiters[1]>"
    condition._waiters.clear()  # Clean up

@pytest.mark.asyncio
async def test_condition_wait_notify(condition):
    async def waiter():
        await condition.wait()

    async def notifier():
        condition.notify()

    await IOLoop.current().run_in_executor(None, lambda: IOLoop.current().run_sync(lambda: waiter()))
    await IOLoop.current().run_in_executor(None, lambda: IOLoop.current().run_sync(lambda: notifier()))

def test_condition_notify_all(condition):
    condition.notify_all()  # Should not raise any exceptions
