# file: lib/ansible/vars/fact_cache.py:30-33
# asked: {"lines": [30, 31, 32, 33], "branches": [[31, 32], [31, 33]]}
# gained: {"lines": [30, 31, 32, 33], "branches": [[31, 32], [31, 33]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError

@pytest.fixture
def fact_cache(monkeypatch):
    plugin = MagicMock()
    monkeypatch.setattr('ansible.vars.fact_cache.cache_loader.get', lambda x: plugin)
    return FactCache()

def test_getitem_key_exists(fact_cache):
    fact_cache._plugin.contains.return_value = True
    fact_cache._plugin.get.return_value = 'value'
    
    assert fact_cache['existing_key'] == 'value'
    fact_cache._plugin.contains.assert_called_once_with('existing_key')
    fact_cache._plugin.get.assert_called_once_with('existing_key')

def test_getitem_key_does_not_exist(fact_cache):
    fact_cache._plugin.contains.return_value = False
    
    with pytest.raises(KeyError):
        fact_cache['non_existing_key']
    fact_cache._plugin.contains.assert_called_once_with('non_existing_key')
