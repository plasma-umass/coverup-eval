# file lib/ansible/vars/fact_cache.py:30-33
# lines [30, 31, 32, 33]
# branches ['31->32', '31->33']

import pytest
from ansible.vars.fact_cache import FactCache
from unittest.mock import MagicMock

@pytest.fixture
def fact_cache_plugin_mock(mocker):
    plugin_mock = MagicMock()
    fact_cache_instance = FactCache()
    fact_cache_instance._plugin = plugin_mock
    return fact_cache_instance

def test_fact_cache_getitem_key_exists(fact_cache_plugin_mock):
    fact_cache_plugin_mock._plugin.contains.return_value = True
    fact_cache_plugin_mock._plugin.get.return_value = 'value'

    assert fact_cache_plugin_mock['existing_key'] == 'value'
    fact_cache_plugin_mock._plugin.contains.assert_called_once_with('existing_key')
    fact_cache_plugin_mock._plugin.get.assert_called_once_with('existing_key')

def test_fact_cache_getitem_keyerror(fact_cache_plugin_mock):
    fact_cache_plugin_mock._plugin.contains.return_value = False

    with pytest.raises(KeyError):
        _ = fact_cache_plugin_mock['non_existing_key']
    fact_cache_plugin_mock._plugin.contains.assert_called_once_with('non_existing_key')
    fact_cache_plugin_mock._plugin.get.assert_not_called()
