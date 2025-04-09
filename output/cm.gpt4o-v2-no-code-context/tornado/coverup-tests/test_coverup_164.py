# file: tornado/locks.py:157-159
# asked: {"lines": [157, 159], "branches": []}
# gained: {"lines": [157, 159], "branches": []}

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_notify_all(condition, mocker):
    mock_notify = mocker.patch.object(condition, 'notify')
    condition._waiters = [1, 2, 3]  # Simulate waiters
    condition.notify_all()
    mock_notify.assert_called_once_with(3)
