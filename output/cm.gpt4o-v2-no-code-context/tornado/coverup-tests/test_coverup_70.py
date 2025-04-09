# file: tornado/locks.py:389-396
# asked: {"lines": [389, 390, 391, 392, 394, 395, 396], "branches": [[394, 395], [394, 396]]}
# gained: {"lines": [389, 390, 391, 392, 394, 395, 396], "branches": [[394, 395], [394, 396]]}

import pytest
from tornado.locks import Semaphore

@pytest.fixture
def semaphore():
    return Semaphore(1)

def test_semaphore_repr_unlocked(semaphore):
    assert "unlocked,value:1" in repr(semaphore)

def test_semaphore_repr_locked(semaphore):
    semaphore.acquire()
    assert "locked" in repr(semaphore)

def test_semaphore_repr_with_waiters(semaphore):
    semaphore.acquire()
    semaphore.acquire()
    assert "locked,waiters:1" in repr(semaphore)

@pytest.fixture(autouse=True)
def cleanup_semaphore(monkeypatch):
    # Ensure that the semaphore is cleaned up after each test
    yield
    monkeypatch.undo()
