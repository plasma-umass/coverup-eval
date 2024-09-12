# file: tornado/locks.py:443-444
# asked: {"lines": [443, 444], "branches": []}
# gained: {"lines": [443, 444], "branches": []}

import pytest
from tornado.locks import Semaphore

def test_semaphore_enter():
    sem = Semaphore()
    with pytest.raises(RuntimeError, match="Use 'async with' instead of 'with' for Semaphore"):
        with sem:
            pass
