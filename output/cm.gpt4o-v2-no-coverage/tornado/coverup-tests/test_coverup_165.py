# file: tornado/locks.py:446-452
# asked: {"lines": [446, 452], "branches": []}
# gained: {"lines": [446, 452], "branches": []}

import pytest
from unittest import mock
from tornado.locks import Semaphore

class TestSemaphore:
    def test_exit_calls_enter(self):
        semaphore = Semaphore()
        with mock.patch.object(semaphore, '__enter__', return_value=None) as mock_enter:
            semaphore.__exit__(None, None, None)
            mock_enter.assert_called_once()

    def test_exit_with_exception(self):
        semaphore = Semaphore()
        with mock.patch.object(semaphore, '__enter__', return_value=None) as mock_enter:
            semaphore.__exit__(ValueError, ValueError("error"), None)
            mock_enter.assert_called_once()
