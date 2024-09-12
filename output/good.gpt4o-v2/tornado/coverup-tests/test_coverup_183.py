# file: tornado/locks.py:454-455
# asked: {"lines": [454, 455], "branches": []}
# gained: {"lines": [454], "branches": []}

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop

@pytest.mark.gen_test
async def test_semaphore_aenter():
    sem = Semaphore(1)
    async with sem:
        assert sem._value == 0
    assert sem._value == 1
