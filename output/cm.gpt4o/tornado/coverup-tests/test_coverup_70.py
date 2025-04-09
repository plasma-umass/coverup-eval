# file tornado/locks.py:389-396
# lines [389, 390, 391, 392, 394, 395, 396]
# branches ['394->395', '394->396']

import pytest
from tornado.locks import Semaphore

@pytest.fixture
def semaphore():
    return Semaphore(1)

def test_semaphore_repr_unlocked(semaphore):
    assert "unlocked,value:1" in repr(semaphore)

def test_semaphore_repr_locked(mocker):
    semaphore = Semaphore(0)
    assert "locked" in repr(semaphore)

def test_semaphore_repr_with_waiters(mocker):
    semaphore = Semaphore(0)
    mocker.patch.object(semaphore, '_waiters', [1, 2, 3])
    assert "locked,waiters:3" in repr(semaphore)

def test_semaphore_repr_unlocked_with_waiters(mocker):
    semaphore = Semaphore(1)
    mocker.patch.object(semaphore, '_waiters', [1, 2])
    assert "unlocked,value:1,waiters:2" in repr(semaphore)
