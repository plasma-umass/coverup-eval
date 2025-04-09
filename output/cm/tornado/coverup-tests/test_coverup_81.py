# file tornado/locks.py:382-387
# lines [382, 383, 384, 385, 387]
# branches ['384->385', '384->387']

import pytest
from tornado.locks import Semaphore

def test_semaphore_initial_value_negative():
    with pytest.raises(ValueError) as exc_info:
        Semaphore(-1)
    assert "semaphore initial value must be >= 0" in str(exc_info.value)
