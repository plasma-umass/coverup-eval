# file: lib/ansible/vars/fact_cache.py:57-59
# asked: {"lines": [57, 59], "branches": []}
# gained: {"lines": [57, 59], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_fact_cache_flush(fact_cache):
    fact_cache.flush()
    fact_cache._plugin.flush.assert_called_once()
