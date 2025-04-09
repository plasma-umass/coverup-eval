# file: tornado/locks.py:565-571
# asked: {"lines": [565, 571], "branches": []}
# gained: {"lines": [565], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aexit():
    lock = Lock()
    lock.release = MagicMock()

    async with lock:
        pass

    lock.release.assert_called_once()

@pytest.mark.asyncio
async def test_lock_aexit_with_exception():
    lock = Lock()
    lock.release = MagicMock()

    class CustomException(Exception):
        pass

    with pytest.raises(CustomException):
        async with lock:
            raise CustomException()

    lock.release.assert_called_once()
