# file: tornado/locks.py:554-560
# asked: {"lines": [560], "branches": []}
# gained: {"lines": [560], "branches": []}

import pytest
from tornado.locks import Lock

def test_lock_exit_calls_enter():
    lock = Lock()
    with pytest.raises(RuntimeError, match="Use `async with` instead of `with` for Lock"):
        lock.__exit__(None, None, None)
