# file: tornado/locks.py:554-560
# asked: {"lines": [554, 560], "branches": []}
# gained: {"lines": [554, 560], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_exit_calls_enter(lock):
    with patch.object(lock, '__enter__', return_value=None) as mock_enter:
        lock.__exit__(None, None, None)
        mock_enter.assert_called_once()

