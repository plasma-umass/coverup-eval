# file: lib/ansible/vars/fact_cache.py:38-39
# asked: {"lines": [38, 39], "branches": []}
# gained: {"lines": [38, 39], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_delitem(fact_cache):
    key = 'test_key'
    fact_cache.__delitem__(key)
    fact_cache._plugin.delete.assert_called_once_with(key)
