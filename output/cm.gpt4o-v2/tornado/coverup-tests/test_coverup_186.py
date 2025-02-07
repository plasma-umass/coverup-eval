# file: tornado/locks.py:551-552
# asked: {"lines": [551, 552], "branches": []}
# gained: {"lines": [551, 552], "branches": []}

import pytest
from tornado.locks import Lock

def test_lock_enter_raises_runtime_error():
    lock = Lock()
    with pytest.raises(RuntimeError, match="Use `async with` instead of `with` for Lock"):
        with lock:
            pass
