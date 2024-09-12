# file: lib/ansible/vars/fact_cache.py:38-39
# asked: {"lines": [38, 39], "branches": []}
# gained: {"lines": [38, 39], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache(monkeypatch):
    mock_plugin = MagicMock()
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader.get', lambda _: mock_plugin)
    return FactCache()

def test_delitem(fact_cache):
    fact_cache._plugin.delete = MagicMock()
    fact_cache.__delitem__('test_key')
    fact_cache._plugin.delete.assert_called_once_with('test_key')
