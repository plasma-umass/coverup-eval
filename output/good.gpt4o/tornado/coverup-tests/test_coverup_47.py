# file tornado/locks.py:466-483
# lines [466, 467, 475, 476, 477, 479, 481, 482, 483]
# branches ['481->482', '481->483']

import pytest
from tornado.locks import BoundedSemaphore

def test_bounded_semaphore_release():
    # Create a BoundedSemaphore with an initial value of 2
    sem = BoundedSemaphore(2)
    
    # Acquire the semaphore twice
    sem.acquire()
    sem.acquire()
    
    # Release the semaphore once, should not raise an error
    sem.release()
    
    # Release the semaphore again, should not raise an error
    sem.release()
    
    # Try to release the semaphore one more time, should raise ValueError
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()
    
    # Clean up: ensure the semaphore is in a consistent state
    assert sem._value == 2

