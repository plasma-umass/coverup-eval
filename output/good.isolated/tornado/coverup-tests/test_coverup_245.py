# file tornado/locks.py:443-444
# lines [444]
# branches []

import pytest
from tornado.locks import Semaphore

def test_semaphore_with_statement_error():
    semaphore = Semaphore()

    with pytest.raises(RuntimeError) as exc_info:
        semaphore.__enter__()

    assert "Use 'async with' instead of 'with' for Semaphore" in str(exc_info.value)
