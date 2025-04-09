# file: lib/ansible/vars/fact_cache.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2', 'key3']
    monkeypatch.setattr('ansible.plugins.loader.cache_loader.get', lambda x: mock_plugin)
    return mock_plugin

def test_fact_cache_len(mock_cache_loader):
    fact_cache = FactCache()
    assert len(fact_cache) == 3
    mock_cache_loader.keys.assert_called_once()

