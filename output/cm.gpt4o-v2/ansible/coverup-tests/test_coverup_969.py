# file: lib/ansible/vars/fact_cache.py:44-45
# asked: {"lines": [44, 45], "branches": []}
# gained: {"lines": [44, 45], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2', 'key3']
    monkeypatch.setattr('ansible.plugins.loader.cache_loader.get', lambda x: mock_plugin)
    return FactCache()

def test_fact_cache_iter(fact_cache):
    keys = list(iter(fact_cache))
    assert keys == ['key1', 'key2', 'key3']
