# file lib/ansible/vars/fact_cache.py:57-59
# lines [57, 59]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_plugin():
    return MagicMock()

@pytest.fixture
def fact_cache(mock_plugin):
    cache = FactCache()
    cache._plugin = mock_plugin
    return cache

def test_fact_cache_flush(fact_cache, mock_plugin):
    fact_cache.flush()
    mock_plugin.flush.assert_called_once()

