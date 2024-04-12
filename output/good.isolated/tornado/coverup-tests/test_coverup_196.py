# file tornado/locks.py:551-552
# lines [551, 552]
# branches []

import pytest
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_with_statement():
    lock = Lock()
    with pytest.raises(RuntimeError) as exc_info:
        with lock:
            pass  # This line should never be reached
    assert "Use `async with` instead of `with` for Lock" in str(exc_info.value)
