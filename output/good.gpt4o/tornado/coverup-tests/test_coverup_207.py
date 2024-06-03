# file tornado/locks.py:446-452
# lines [446, 452]
# branches []

import pytest
from tornado.locks import Semaphore

def test_semaphore_exit():
    semaphore = Semaphore()
    with pytest.raises(RuntimeError):
        with semaphore:
            raise RuntimeError("Test exception")

    assert semaphore._timeouts is not None
