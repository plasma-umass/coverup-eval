# file lib/ansible/vars/fact_cache.py:47-48
# lines [47, 48]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_plugin():
    plugin = MagicMock()
    plugin.keys.return_value = ['key1', 'key2', 'key3']
    return plugin

@pytest.fixture
def fact_cache(mock_plugin):
    cache = FactCache()
    cache._plugin = mock_plugin
    return cache

def test_fact_cache_len(fact_cache, mock_plugin):
    assert len(fact_cache) == 3
    mock_plugin.keys.assert_called_once()

