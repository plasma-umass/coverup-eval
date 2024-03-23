# file tornado/locks.py:389-396
# lines [389, 390, 391, 392, 394, 395, 396]
# branches ['394->395', '394->396']

import pytest
from tornado.locks import Semaphore

@pytest.fixture
def semaphore():
    return Semaphore(value=2)

@pytest.fixture
def locked_semaphore():
    sem = Semaphore(value=0)
    sem._waiters = ['fake_waiter']
    return sem

def test_semaphore_repr_unlocked(semaphore):
    repr_str = repr(semaphore)
    assert "unlocked,value:2" in repr_str
    assert "waiters" not in repr_str

def test_semaphore_repr_locked_no_waiters(locked_semaphore):
    # Temporarily remove fake waiter for this test
    locked_semaphore._waiters.pop()
    repr_str = repr(locked_semaphore)
    assert "locked" in repr_str
    assert "waiters" not in repr_str

def test_semaphore_repr_locked_with_waiters(locked_semaphore):
    repr_str = repr(locked_semaphore)
    assert "locked" in repr_str
    assert "waiters:1" in repr_str
