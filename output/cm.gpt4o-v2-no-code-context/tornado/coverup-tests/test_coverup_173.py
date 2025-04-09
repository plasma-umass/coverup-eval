# file: tornado/locks.py:565-571
# asked: {"lines": [565, 571], "branches": []}
# gained: {"lines": [565], "branches": []}

import pytest
import tornado.locks
import types

@pytest.mark.asyncio
async def test_lock_aexit():
    lock = tornado.locks.Lock()
    await lock.acquire()
    assert lock.locked()

    # Simulate the __aexit__ call
    await lock.__aexit__(None, None, None)
    assert not lock.locked()

@pytest.mark.asyncio
async def test_lock_aexit_with_exception():
    lock = tornado.locks.Lock()
    await lock.acquire()
    assert lock.locked()

    # Simulate the __aexit__ call with an exception
    await lock.__aexit__(Exception, Exception("test"), None)
    assert not lock.locked()
