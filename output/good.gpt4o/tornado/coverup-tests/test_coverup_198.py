# file tornado/locks.py:457-463
# lines [457, 463]
# branches []

import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_aexit(mocker):
    sem = Semaphore(1)
    sem.release = mocker.Mock()

    async with sem:
        pass

    sem.release.assert_called_once()
