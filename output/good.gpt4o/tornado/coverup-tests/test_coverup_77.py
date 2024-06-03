# file tornado/locks.py:117-121
# lines [117, 118, 119, 120, 121]
# branches ['119->120', '119->121']

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_condition_repr_no_waiters(condition):
    # Test __repr__ when there are no waiters
    repr_str = repr(condition)
    assert repr_str == "<Condition>"

def test_condition_repr_with_waiters(mocker, condition):
    # Mock the _waiters attribute to simulate waiters
    mocker.patch.object(condition, '_waiters', new_callable=list)
    condition._waiters.extend([None, None])  # Simulate 2 waiters
    repr_str = repr(condition)
    assert repr_str == "<Condition waiters[2]>"

