# file: lib/ansible/vars/fact_cache.py:35-36
# asked: {"lines": [35, 36], "branches": []}
# gained: {"lines": [35, 36], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(monkeypatch):
    mock_plugin = MagicMock()
    mock_plugin.set = MagicMock()
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader.get', lambda x: mock_plugin)
    return mock_plugin

def test_fact_cache_setitem(mock_cache_loader):
    fact_cache = FactCache()
    fact_cache['test_key'] = 'test_value'
    mock_cache_loader.set.assert_called_once_with('test_key', 'test_value')
