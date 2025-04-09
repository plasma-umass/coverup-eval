# file: lib/ansible/vars/fact_cache.py:44-45
# asked: {"lines": [44, 45], "branches": []}
# gained: {"lines": [44, 45], "branches": []}

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

def test_fact_cache_iter(fact_cache):
    keys = list(iter(fact_cache))
    assert keys == ['key1', 'key2', 'key3']
