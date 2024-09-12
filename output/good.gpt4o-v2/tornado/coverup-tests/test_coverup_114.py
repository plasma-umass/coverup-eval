# file: tornado/locks.py:539-549
# asked: {"lines": [539, 546, 547, 548, 549], "branches": []}
# gained: {"lines": [539, 546, 547, 548, 549], "branches": []}

import pytest
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_release_when_locked():
    lock = Lock()
    await lock.acquire()
    lock.release()
    assert lock._block._value == 1, "Lock should be released"

def test_lock_release_when_unlocked():
    lock = Lock()
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()
