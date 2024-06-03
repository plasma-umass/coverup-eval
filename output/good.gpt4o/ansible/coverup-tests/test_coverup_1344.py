# file lib/ansible/vars/fact_cache.py:41-42
# lines [42]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_fact_cache_contains(fact_cache):
    key = 'test_key'
    fact_cache._plugin.contains.return_value = True

    assert key in fact_cache
    fact_cache._plugin.contains.assert_called_once_with(key)
