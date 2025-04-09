# file: lib/ansible/vars/fact_cache.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_plugin():
    plugin = MagicMock()
    plugin.contains.return_value = True
    plugin.get.return_value = 'value'
    plugin.keys.return_value = ['key1', 'key2']
    return plugin

@pytest.fixture
def fact_cache(mock_plugin):
    with patch('ansible.vars.fact_cache.cache_loader.get', return_value=mock_plugin):
        return FactCache()

def test_fact_cache_init_no_plugin():
    with patch('ansible.vars.fact_cache.cache_loader.get', return_value=None):
        with pytest.raises(AnsibleError, match='Unable to load the facts cache plugin'):
            FactCache()

def test_fact_cache_copy(fact_cache, mock_plugin):
    copy = fact_cache.copy()
    assert copy == {'key1': 'value', 'key2': 'value'}

def test_fact_cache_getitem(fact_cache, mock_plugin):
    assert fact_cache['key1'] == 'value'
    mock_plugin.contains.assert_called_once_with('key1')
    mock_plugin.get.assert_called_once_with('key1')

def test_fact_cache_getitem_keyerror(fact_cache, mock_plugin):
    mock_plugin.contains.return_value = False
    with pytest.raises(KeyError):
        fact_cache['nonexistent_key']

def test_fact_cache_setitem(fact_cache, mock_plugin):
    fact_cache['key3'] = 'new_value'
    mock_plugin.set.assert_called_once_with('key3', 'new_value')

def test_fact_cache_delitem(fact_cache, mock_plugin):
    del fact_cache['key1']
    mock_plugin.delete.assert_called_once_with('key1')

def test_fact_cache_iter(fact_cache, mock_plugin):
    keys = list(iter(fact_cache))
    assert keys == ['key1', 'key2']
    mock_plugin.keys.assert_called_once()

def test_fact_cache_len(fact_cache, mock_plugin):
    assert len(fact_cache) == 2
    mock_plugin.keys.assert_called_once()
