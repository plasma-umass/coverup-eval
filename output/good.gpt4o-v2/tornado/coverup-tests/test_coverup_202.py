# file: tornado/locks.py:145-155
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 151], [154, 0], [154, 155]]}

import pytest
from unittest.mock import Mock, MagicMock
from tornado.locks import Condition
from tornado.concurrent import Future
from collections import deque

@pytest.fixture
def condition():
    cond = Condition()
    cond._waiters = deque()
    return cond

def test_notify_executes_all_branches(condition):
    # Create Future objects
    future1 = Future()
    future2 = Future()
    future3 = Future()
    
    # Add futures to the _waiters deque
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    condition._waiters.append(future3)
    
    # Call notify with n=2
    condition.notify(n=2)
    
    # Check that the correct futures were set
    assert future1.done()
    assert future1.result() == True
    assert future2.done()
    assert future2.result() == True
    assert not future3.done()
    
    # Ensure that the _waiters deque has the remaining futures
    assert list(condition._waiters) == [future3]
