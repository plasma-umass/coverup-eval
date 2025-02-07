# file: lib/ansible/galaxy/api.py:48-53
# asked: {"lines": [48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 53], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.galaxy.api import cache_lock

@pytest.fixture
def mock_lock(monkeypatch):
    mock_lock = Mock()
    mock_lock.__enter__ = Mock()
    mock_lock.__exit__ = Mock()
    monkeypatch.setattr('ansible.galaxy.api._CACHE_LOCK', mock_lock)
    return mock_lock

def test_cache_lock_decorator(mock_lock):
    @cache_lock
    def test_func(x):
        return x * 2

    result = test_func(5)
    assert result == 10
    mock_lock.__enter__.assert_called_once()
    mock_lock.__exit__.assert_called_once()
