# file: tornado/locks.py:446-452
# asked: {"lines": [446, 452], "branches": []}
# gained: {"lines": [446], "branches": []}

import pytest
from tornado.locks import Semaphore
import asyncio

class TestSemaphore:
    @pytest.mark.asyncio
    async def test_semaphore_exit(self):
        semaphore = Semaphore()

        class MockException(Exception):
            pass

        with pytest.raises(MockException):
            async with semaphore:
                raise MockException()

        assert semaphore._value == 1  # Assuming initial value is 1

    @pytest.mark.asyncio
    async def test_semaphore_exit_no_exception(self):
        semaphore = Semaphore()

        async with semaphore:
            pass

        assert semaphore._value == 1  # Assuming initial value is 1
