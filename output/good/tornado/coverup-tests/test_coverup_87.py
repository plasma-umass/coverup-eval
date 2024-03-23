# file tornado/locks.py:117-121
# lines [117, 118, 119, 120, 121]
# branches ['119->120', '119->121']

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_condition_repr_with_waiters(condition, mocker):
    # Mock a waiter to simulate the presence of waiters
    fake_waiter = mocker.MagicMock()
    condition._waiters.append(fake_waiter)

    # Check the __repr__ output when there are waiters
    assert "waiters[1]" in repr(condition)

    # Clean up by removing the fake waiter
    condition._waiters.remove(fake_waiter)

def test_condition_repr_without_waiters(condition):
    # Check the __repr__ output when there are no waiters
    assert "waiters" not in repr(condition)
    assert "<Condition>" == repr(condition)
