# file tornado/locks.py:262-283
# lines [262, 263, 271, 272, 274, 275, 277, 283]
# branches []

import pytest
from tornado.locks import Semaphore
from unittest.mock import MagicMock

@pytest.fixture
def mock_semaphore():
    semaphore = Semaphore(1)
    semaphore.release = MagicMock()
    return semaphore

@pytest.mark.asyncio
async def test_releasing_context_manager(mock_semaphore):
    async with mock_semaphore.acquire():
        pass
    mock_semaphore.release.assert_called_once()
