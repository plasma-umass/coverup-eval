# file: tornado/locks.py:565-571
# asked: {"lines": [565, 571], "branches": []}
# gained: {"lines": [565], "branches": []}

import pytest
import types
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aexit_no_exception(mocker):
    lock = Lock()
    mock_release = mocker.patch.object(lock, 'release')
    
    await lock.__aexit__(None, None, None)
    
    mock_release.assert_called_once()

@pytest.mark.asyncio
async def test_lock_aexit_with_exception(mocker):
    lock = Lock()
    mock_release = mocker.patch.object(lock, 'release')
    
    await lock.__aexit__(Exception, Exception("error"), types.TracebackType)
    
    mock_release.assert_called_once()
