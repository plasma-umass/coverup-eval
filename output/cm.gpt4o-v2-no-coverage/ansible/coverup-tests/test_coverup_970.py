# file: lib/ansible/vars/fact_cache.py:44-45
# asked: {"lines": [44, 45], "branches": []}
# gained: {"lines": [44, 45], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import cache_loader
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2', 'key3']
    monkeypatch.setattr(cache_loader, 'get', lambda x: mock_plugin)
    return mock_plugin

def test_fact_cache_iter(mock_cache_loader):
    fact_cache = FactCache()
    keys = list(fact_cache)
    assert keys == ['key1', 'key2', 'key3']

def test_fact_cache_no_plugin(monkeypatch):
    monkeypatch.setattr(cache_loader, 'get', lambda x: None)
    with pytest.raises(AnsibleError, match='Unable to load the facts cache plugin'):
        FactCache()
