# file: lib/ansible/vars/fact_cache.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2']
    mock_plugin.get.side_effect = lambda key: {'key1': 'value1', 'key2': 'value2'}[key]
    mock_plugin.contains.side_effect = lambda key: key in ['key1', 'key2']
    monkeypatch.setattr('ansible.plugins.loader.cache_loader.get', lambda _: mock_plugin)
    return FactCache()

def test_fact_cache_copy(fact_cache):
    # Set up initial state
    fact_cache['key1'] = 'value1'
    fact_cache['key2'] = 'value2'
    
    # Call the method
    copied_cache = fact_cache.copy()
    
    # Assertions
    assert copied_cache == {'key1': 'value1', 'key2': 'value2'}
    assert isinstance(copied_cache, dict)

    # Clean up
    fact_cache.flush()
