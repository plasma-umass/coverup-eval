# file tornado/locks.py:382-387
# lines [382, 383, 384, 385, 387]
# branches ['384->385', '384->387']

import pytest
from tornado.locks import Semaphore

def test_semaphore_initial_value_negative():
    with pytest.raises(ValueError, match="semaphore initial value must be >= 0"):
        Semaphore(-1)

def test_semaphore_initial_value_zero():
    sem = Semaphore(0)
    assert sem._value == 0

def test_semaphore_initial_value_positive():
    sem = Semaphore(5)
    assert sem._value == 5
