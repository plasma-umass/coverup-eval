# file lib/ansible/vars/fact_cache.py:54-55
# lines [55]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    mock_plugin = MagicMock()
    mock_plugin.keys.return_value = ['key1', 'key2', 'key3']
    cache = FactCache()
    cache._plugin = mock_plugin
    return cache

def test_fact_cache_keys(fact_cache):
    keys = fact_cache.keys()
    assert keys == ['key1', 'key2', 'key3']
    fact_cache._plugin.keys.assert_called_once()

@pytest.fixture(autouse=True)
def cleanup_fact_cache(fact_cache):
    yield
    fact_cache._plugin.reset_mock()
