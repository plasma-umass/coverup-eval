# file lib/ansible/vars/fact_cache.py:44-45
# lines [44, 45]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    cache._plugin.keys.return_value = ['key1', 'key2', 'key3']
    return cache

def test_fact_cache_iter(fact_cache):
    keys = list(iter(fact_cache))
    assert keys == ['key1', 'key2', 'key3']
