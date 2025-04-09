# file tornado/locks.py:157-159
# lines [157, 159]
# branches []

import pytest
from tornado.locks import Condition
from unittest.mock import MagicMock

@pytest.fixture
def condition():
    return Condition()

def test_notify_all(condition, mocker):
    mock_notify = mocker.patch.object(condition, 'notify')
    condition._waiters = [MagicMock(), MagicMock(), MagicMock()]
    
    condition.notify_all()
    
    mock_notify.assert_called_once_with(len(condition._waiters))
