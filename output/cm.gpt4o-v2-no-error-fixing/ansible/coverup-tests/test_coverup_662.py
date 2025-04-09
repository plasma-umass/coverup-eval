# file: lib/ansible/vars/fact_cache.py:38-39
# asked: {"lines": [38, 39], "branches": []}
# gained: {"lines": [38, 39], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    # Mock the cache_loader and the plugin
    mock_plugin = MagicMock()
    mock_cache_loader = MagicMock()
    mock_cache_loader.get.return_value = mock_plugin
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader', mock_cache_loader)
    
    # Create an instance of FactCache
    return FactCache()

def test_delitem(fact_cache):
    key = 'test_key'
    
    # Perform the deletion
    del fact_cache[key]
    
    # Assert that the delete method was called on the plugin
    fact_cache._plugin.delete.assert_called_once_with(key)
