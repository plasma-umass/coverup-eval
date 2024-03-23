# file tornado/locks.py:466-483
# lines [466, 467, 475, 476, 477, 479, 481, 482, 483]
# branches ['481->482', '481->483']

import pytest
from tornado.locks import BoundedSemaphore

@pytest.fixture
def bounded_semaphore():
    return BoundedSemaphore(value=2)

def test_bounded_semaphore_release_too_many_times(bounded_semaphore):
    # Acquire the semaphore twice to reach the limit
    bounded_semaphore.acquire()
    bounded_semaphore.acquire()
    
    # Release the semaphore twice, which should be fine
    bounded_semaphore.release()
    bounded_semaphore.release()
    
    # The third release should raise a ValueError
    with pytest.raises(ValueError) as exc_info:
        bounded_semaphore.release()
    assert str(exc_info.value) == "Semaphore released too many times"
