# file: lib/ansible/vars/fact_cache.py:41-42
# asked: {"lines": [41, 42], "branches": []}
# gained: {"lines": [41, 42], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader.get', lambda _: mock_plugin)
    return FactCache()

def test_fact_cache_contains(fact_cache):
    fact_cache._plugin.contains.return_value = True
    assert 'some_key' in fact_cache
    fact_cache._plugin.contains.assert_called_once_with('some_key')

    fact_cache._plugin.contains.return_value = False
    assert 'some_other_key' not in fact_cache
    fact_cache._plugin.contains.assert_called_with('some_other_key')
