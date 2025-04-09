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
    
    # Use the __aexit__ method directly to simulate exiting an async context
    await sem.__aexit__(None, None, None)
    
    # Assert that the semaphore can be acquired again, meaning it was released
    assert sem._value == 1
