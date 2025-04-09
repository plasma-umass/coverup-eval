# file: lib/ansible/vars/fact_cache.py:61-72
# asked: {"lines": [62, 64, 65, 66, 67, 68, 69, 70, 72], "branches": [[66, 67], [66, 72]]}
# gained: {"lines": [62, 64, 65, 66, 67, 68, 69, 70, 72], "branches": [[66, 67]]}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader.get', lambda x: mock_plugin)
    return FactCache()

def test_first_order_merge_with_existing_key(fact_cache):
    fact_cache._plugin.get.return_value = {'existing_key': 'existing_value'}
    fact_cache.first_order_merge('existing_key', {'new_key': 'new_value'})
    fact_cache._plugin.get.assert_called_once_with('existing_key')
    assert fact_cache._plugin.get.return_value == {'existing_key': 'existing_value', 'new_key': 'new_value'}

def test_first_order_merge_with_non_existing_key(fact_cache):
    fact_cache._plugin.get.side_effect = KeyError
    fact_cache.first_order_merge('non_existing_key', {'new_key': 'new_value'})
    fact_cache._plugin.get.assert_called_once_with('non_existing_key')
    assert fact_cache._plugin.get.side_effect == KeyError
