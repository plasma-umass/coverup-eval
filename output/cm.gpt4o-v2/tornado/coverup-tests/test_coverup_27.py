# file: tornado/locks.py:145-155
# asked: {"lines": [145, 147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}
# gained: {"lines": [145], "branches": []}

import pytest
from tornado.locks import Condition
from tornado.concurrent import Future

@pytest.mark.gen_test
async def test_condition_notify():
    condition = Condition()
    waiter1 = Future()
    waiter2 = Future()
    
    condition._waiters.append(waiter1)
    condition._waiters.append(waiter2)
    
    condition.notify(2)
    
    assert waiter1.done()
    assert waiter2.done()
    assert waiter1.result() is True
    assert waiter2.result() is True
