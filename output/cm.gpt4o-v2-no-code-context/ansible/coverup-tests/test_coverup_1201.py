# file: lib/ansible/vars/fact_cache.py:57-59
# asked: {"lines": [59], "branches": []}
# gained: {"lines": [59], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_flush(fact_cache):
    fact_cache.flush()
    fact_cache._plugin.flush.assert_called_once()

