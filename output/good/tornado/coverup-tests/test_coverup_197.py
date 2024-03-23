# file tornado/locks.py:565-571
# lines [565, 571]
# branches []

import pytest
from tornado.locks import Lock
from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_lock_aexit():
    lock = Lock()
    lock.release = MagicMock()

    # Simulate entering the context manager
    async with lock:
        # The __aexit__ method will be called upon exiting this block
        pass

    # Assert that release was called once by the __aexit__ method
    lock.release.assert_called_once()

    # Clean up is not necessary here as we are using a MagicMock
    # which is automatically garbage collected
