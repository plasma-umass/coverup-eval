# file: tornado/locks.py:466-483
# asked: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}
# gained: {"lines": [466, 467, 475, 479], "branches": []}

import pytest
from tornado.locks import BoundedSemaphore

@pytest.mark.asyncio
async def test_bounded_semaphore_initial_value():
    sem = BoundedSemaphore(2)
    assert sem._initial_value == 2

@pytest.mark.asyncio
async def test_bounded_semaphore_release_within_limit():
    sem = BoundedSemaphore(2)
    await sem.acquire()  # Decrease the semaphore value
    sem.release()  # This should not raise an error
    assert sem._value == 2

@pytest.mark.asyncio
async def test_bounded_semaphore_release_exceeding_limit():
    sem = BoundedSemaphore(1)
    await sem.acquire()  # Decrease the semaphore value
    sem.release()  # This should not raise an error
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()
