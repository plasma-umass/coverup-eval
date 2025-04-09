# file: tornado/locks.py:457-463
# asked: {"lines": [457, 463], "branches": []}
# gained: {"lines": [457], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_aexit():
    sem = Semaphore()
    sem.release = MagicMock()

    async with sem:
        pass

    sem.release.assert_called_once()
