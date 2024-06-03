# file tornado/locks.py:565-571
# lines [565, 571]
# branches []

import pytest
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aexit(mocker):
    lock = Lock()
    mock_release = mocker.patch.object(lock, 'release')

    # Simulate the __aexit__ method call
    await lock.__aexit__(None, None, None)

    # Assert that release was called
    mock_release.assert_called_once()
