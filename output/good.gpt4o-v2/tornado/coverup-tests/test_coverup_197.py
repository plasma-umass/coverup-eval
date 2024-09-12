# file: tornado/locks.py:565-571
# asked: {"lines": [565, 571], "branches": []}
# gained: {"lines": [565], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
import types
from typing import Optional
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aexit():
    lock = Lock()
    lock.release = MagicMock()

    await lock.__aexit__(None, None, None)

    lock.release.assert_called_once()

@pytest.mark.asyncio
async def test_lock_aexit_with_exception():
    lock = Lock()
    lock.release = MagicMock()

    await lock.__aexit__(RuntimeError, RuntimeError("error"), None)

    lock.release.assert_called_once()

def test_lock_release():
    lock = Lock()
    lock._block.release = MagicMock()

    lock.release()

    lock._block.release.assert_called_once()

def test_lock_release_unlocked():
    lock = Lock()
    lock._block.release = MagicMock(side_effect=ValueError)

    with pytest.raises(RuntimeError, match='release unlocked lock'):
        lock.release()
