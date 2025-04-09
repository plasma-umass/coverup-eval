# file: lib/ansible/vars/fact_cache.py:44-45
# asked: {"lines": [45], "branches": []}
# gained: {"lines": [45], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_fact_cache_iter(fact_cache):
    fact_cache._plugin.keys.return_value = ['key1', 'key2', 'key3']
    keys = list(iter(fact_cache))
    assert keys == ['key1', 'key2', 'key3']
    fact_cache._plugin.keys.assert_called_once()

