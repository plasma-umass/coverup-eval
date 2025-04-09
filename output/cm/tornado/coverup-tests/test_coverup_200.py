# file tornado/locks.py:486-522
# lines [486, 487]
# branches []

import pytest
from tornado.locks import Lock
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
async def test_lock_release_unacquired():
    lock = Lock()
    with pytest.raises(RuntimeError):
        lock.release()

@pytest.mark.gen_test
async def test_lock_acquire_context_manager():
    lock = Lock()
    async with lock.acquire():
        assert lock._locked
    assert not lock._locked

@pytest.mark.gen_test
async def test_lock_acquire_with_yield():
    lock = Lock()
    with (await lock.acquire()):
        assert lock._locked
    assert not lock._locked
