# file tornado/locks.py:145-155
# lines [145, 147, 148, 149, 150, 151, 152, 154, 155]
# branches ['148->149', '148->154', '150->148', '150->151', '154->exit', '154->155']

import pytest
from tornado.locks import Condition
from tornado.concurrent import Future

@pytest.fixture
def condition():
    return Condition()

def test_notify(condition):
    # Create mock futures to act as waiters
    future1 = Future()
    future2 = Future()
    future3 = Future()

    # Add futures to the condition's waiters
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    condition._waiters.append(future3)

    # Notify 2 waiters
    condition.notify(2)

    # Check that the first two futures are done
    assert future1.done()
    assert future2.done()
    assert not future3.done()

    # Check the result of the futures
    assert future1.result() is True
    assert future2.result() is True

    # Clean up
    future1.cancel()
    future2.cancel()
    future3.cancel()
