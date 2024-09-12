# file: tornado/locks.py:157-159
# asked: {"lines": [159], "branches": []}
# gained: {"lines": [159], "branches": []}

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_notify_all(condition, mocker):
    mock_notify = mocker.patch.object(condition, 'notify')
    condition.notify_all()
    mock_notify.assert_called_once_with(len(condition._waiters))
