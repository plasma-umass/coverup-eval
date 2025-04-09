# file: lib/ansible/vars/fact_cache.py:41-42
# asked: {"lines": [41, 42], "branches": []}
# gained: {"lines": [41, 42], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_contains_key_present(fact_cache):
    fact_cache._plugin.contains.return_value = True
    assert 'some_key' in fact_cache
    fact_cache._plugin.contains.assert_called_once_with('some_key')

def test_contains_key_absent(fact_cache):
    fact_cache._plugin.contains.return_value = False
    assert 'some_key' not in fact_cache
    fact_cache._plugin.contains.assert_called_once_with('some_key')
