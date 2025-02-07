# file: lib/ansible/vars/fact_cache.py:35-36
# asked: {"lines": [35, 36], "branches": []}
# gained: {"lines": [35, 36], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.cache_loader.get', lambda _: mock_plugin)
    return FactCache()

def test_setitem(fact_cache):
    key = 'test_key'
    value = 'test_value'
    
    fact_cache[key] = value
    
    fact_cache._plugin.set.assert_called_once_with(key, value)
