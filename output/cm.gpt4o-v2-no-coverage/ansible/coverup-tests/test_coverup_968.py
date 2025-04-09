# file: lib/ansible/vars/fact_cache.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    fc = FactCache()
    fc._plugin = MagicMock()
    return fc

def test_fact_cache_len(fact_cache):
    fact_cache._plugin.keys.return_value = ['a', 'b', 'c']
    assert len(fact_cache) == 3
    fact_cache._plugin.keys.assert_called_once()
