# file: lib/ansible/vars/fact_cache.py:30-33
# asked: {"lines": [30, 31, 32, 33], "branches": [[31, 32], [31, 33]]}
# gained: {"lines": [30, 31, 32, 33], "branches": [[31, 32], [31, 33]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache():
    with patch('ansible.vars.fact_cache.cache_loader.get') as mock_cache_loader:
        mock_plugin = MagicMock()
        mock_cache_loader.return_value = mock_plugin
        yield FactCache(), mock_plugin

def test_getitem_key_exists(fact_cache):
    cache, mock_plugin = fact_cache
    mock_plugin.contains.return_value = True
    mock_plugin.get.return_value = 'value'
    
    assert cache['key'] == 'value'
    mock_plugin.contains.assert_called_once_with('key')
    mock_plugin.get.assert_called_once_with('key')

def test_getitem_key_does_not_exist(fact_cache):
    cache, mock_plugin = fact_cache
    mock_plugin.contains.return_value = False
    
    with pytest.raises(KeyError):
        cache['nonexistent_key']
    mock_plugin.contains.assert_called_once_with('nonexistent_key')
