# file: lib/ansible/vars/fact_cache.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2', 'key3']
    monkeypatch.setattr('ansible.plugins.loader.cache_loader.get', lambda x: mock_plugin)
    return mock_plugin

def test_fact_cache_keys(mock_cache_loader):
    fact_cache = FactCache()
    keys = fact_cache.keys()
    assert keys == ['key1', 'key2', 'key3']
    mock_cache_loader.keys.assert_called_once()
