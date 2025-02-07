# file: lib/ansible/vars/fact_cache.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    cache_plugin = MagicMock()
    cache_plugin.keys.return_value = ['key1', 'key2', 'key3']
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('ansible.plugins.loader.cache_loader.get', lambda x: cache_plugin)
        yield FactCache()

def test_fact_cache_len(fact_cache):
    assert len(fact_cache) == 3
