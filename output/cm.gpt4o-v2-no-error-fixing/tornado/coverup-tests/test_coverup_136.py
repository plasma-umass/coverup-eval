# file: tornado/locks.py:457-463
# asked: {"lines": [457, 463], "branches": []}
# gained: {"lines": [457], "branches": []}

import pytest
from tornado.locks import Semaphore
from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_semaphore_aexit():
    sem = Semaphore(1)
    sem.release = MagicMock()

    async with sem:
        pass

    sem.release.assert_called_once()
