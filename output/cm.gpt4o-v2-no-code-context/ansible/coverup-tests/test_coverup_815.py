# file: lib/ansible/vars/fact_cache.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

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

def test_fact_cache_len(fact_cache):
    assert len(fact_cache) == 3
