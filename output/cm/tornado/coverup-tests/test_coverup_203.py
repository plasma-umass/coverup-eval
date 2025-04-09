# file tornado/locks.py:457-463
# lines [457, 463]
# branches []

import asyncio
import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_context_manager():
    semaphore = Semaphore(value=1)
    async with semaphore:
        assert semaphore._value == 0  # The semaphore is acquired

    # After the async with block, the semaphore should be released
    assert semaphore._value == 1

    # Now we'll test the __aexit__ without the context manager
    await semaphore.acquire()
    assert semaphore._value == 0  # The semaphore is acquired
    await semaphore.__aexit__(None, None, None)
    assert semaphore._value == 1  # The semaphore should be released
