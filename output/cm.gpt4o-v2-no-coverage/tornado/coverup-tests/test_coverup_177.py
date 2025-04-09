# file: tornado/locks.py:398-413
# asked: {"lines": [402, 403, 404, 412, 413], "branches": [[401, 402], [403, 401], [403, 404]]}
# gained: {"lines": [402, 403, 404, 412, 413], "branches": [[401, 402], [403, 401], [403, 404]]}

import pytest
from tornado.locks import Semaphore
from unittest.mock import Mock

@pytest.fixture
def semaphore():
    return Semaphore()

def test_semaphore_release_no_waiters(semaphore):
    initial_value = semaphore._value
    semaphore.release()
    assert semaphore._value == initial_value + 1

def test_semaphore_release_with_waiters(semaphore, mocker):
    mock_waiter = Mock()
    mock_waiter.done.return_value = False
    semaphore._waiters.append(mock_waiter)
    initial_value = semaphore._value
    semaphore.release()
    assert semaphore._value == initial_value
    mock_waiter.set_result.assert_called_once()
    assert semaphore._value == initial_value

def test_semaphore_release_with_done_waiters(semaphore, mocker):
    mock_waiter = Mock()
    mock_waiter.done.return_value = True
    semaphore._waiters.append(mock_waiter)
    initial_value = semaphore._value
    semaphore.release()
    assert semaphore._value == initial_value + 1
    mock_waiter.set_result.assert_not_called()
