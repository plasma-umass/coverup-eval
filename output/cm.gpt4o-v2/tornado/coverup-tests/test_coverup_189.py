# file: tornado/locks.py:562-563
# asked: {"lines": [562, 563], "branches": []}
# gained: {"lines": [562], "branches": []}

import pytest
from tornado.locks import Lock
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_lock_aenter():
    lock = Lock()
    
    with patch.object(lock, 'acquire', new_callable=AsyncMock) as mock_acquire:
        await lock.__aenter__()
        mock_acquire.assert_awaited_once()
