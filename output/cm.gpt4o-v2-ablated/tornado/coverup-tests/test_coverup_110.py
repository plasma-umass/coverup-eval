# file: tornado/locks.py:457-463
# asked: {"lines": [457, 463], "branches": []}
# gained: {"lines": [457], "branches": []}

import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_aexit():
    sem = Semaphore(1)
    
    # Acquire the semaphore to ensure it needs to be released
    await sem.acquire()
    assert sem._value == 0  # Ensure the semaphore is acquired

    # Use __aexit__ to release the semaphore
    await sem.__aexit__(None, None, None)
    assert sem._value == 1  # Ensure the semaphore is released
