# file tornado/locks.py:551-552
# lines [552]
# branches []

import pytest
from tornado.locks import Lock

def test_lock_with_statement():
    lock = Lock()
    with pytest.raises(RuntimeError) as exc_info:
        lock.__enter__()
    assert "Use `async with` instead of `with` for Lock" in str(exc_info.value)
