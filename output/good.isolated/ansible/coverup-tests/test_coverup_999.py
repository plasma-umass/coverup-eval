# file lib/ansible/vars/fact_cache.py:44-45
# lines [44, 45]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

# Assuming the FactCache class has a _plugin attribute that is a dict or dict-like object

@pytest.fixture
def fact_cache(mocker):
    plugin_mock = mocker.MagicMock()
    plugin_mock.keys.return_value = ['host1', 'host2', 'host3']
    fact_cache_instance = FactCache()
    fact_cache_instance._plugin = plugin_mock
    return fact_cache_instance

def test_fact_cache_iter(fact_cache):
    # Test the __iter__ method of FactCache
    keys = list(iter(fact_cache))
    assert keys == ['host1', 'host2', 'host3']
    fact_cache._plugin.keys.assert_called_once()
