# file lib/ansible/vars/fact_cache.py:30-33
# lines [31, 32, 33]
# branches ['31->32', '31->33']

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError

@pytest.fixture
def mock_plugin():
    plugin = MagicMock()
    return plugin

@pytest.fixture
def fact_cache(mock_plugin):
    with patch('ansible.vars.fact_cache.cache_loader.get', return_value=mock_plugin):
        return FactCache()

def test_fact_cache_key_error(fact_cache, mock_plugin):
    mock_plugin.contains.return_value = False
    with pytest.raises(KeyError):
        fact_cache['nonexistent_key']

def test_fact_cache_get_item(fact_cache, mock_plugin):
    mock_plugin.contains.return_value = True
    mock_plugin.get.return_value = 'value'
    assert fact_cache['existent_key'] == 'value'
    mock_plugin.get.assert_called_once_with('existent_key')
