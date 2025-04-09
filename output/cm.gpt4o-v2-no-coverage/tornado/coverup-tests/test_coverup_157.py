# file: tornado/locks.py:157-159
# asked: {"lines": [157, 159], "branches": []}
# gained: {"lines": [157, 159], "branches": []}

import pytest
from collections import deque
from tornado.locks import Condition

class TestCondition:
    @pytest.fixture
    def condition(self):
        cond = Condition()
        cond._waiters = deque([1, 2, 3])  # Simulate some waiters
        return cond

    def test_notify_all(self, condition, mocker):
        mock_notify = mocker.patch.object(condition, 'notify')
        condition.notify_all()
        mock_notify.assert_called_once_with(3)
