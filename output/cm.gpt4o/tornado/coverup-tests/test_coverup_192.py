# file tornado/locks.py:443-444
# lines [443, 444]
# branches []

import pytest
from tornado.locks import Semaphore

def test_semaphore_enter():
    semaphore = Semaphore()
    with pytest.raises(RuntimeError, match="Use 'async with' instead of 'with' for Semaphore"):
        with semaphore:
            pass
