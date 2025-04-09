# file: tornado/locks.py:389-396
# asked: {"lines": [389, 390, 391, 392, 394, 395, 396], "branches": [[394, 395], [394, 396]]}
# gained: {"lines": [389], "branches": []}

import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_repr():
    sem = Semaphore(1)
    assert repr(sem) == "<Semaphore [unlocked,value:1]>"

    sem = Semaphore(0)
    assert repr(sem) == "<Semaphore [locked]>"

    sem._waiters.append(None)
    assert repr(sem) == "<Semaphore [locked,waiters:1]>"

    sem = Semaphore(2)
    sem._waiters.append(None)
    assert repr(sem) == "<Semaphore [unlocked,value:2,waiters:1]>"
