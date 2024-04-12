# file lib/ansible/vars/fact_cache.py:35-36
# lines [35, 36]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def fact_cache_instance(mocker):
    plugin_mock = mocker.MagicMock()
    fact_cache = FactCache()
    mocker.patch.object(fact_cache, '_plugin', new=plugin_mock)
    return fact_cache

def test_fact_cache_setitem(fact_cache_instance):
    key = 'test_key'
    value = 'test_value'
    fact_cache_instance.__setitem__(key, value)
    fact_cache_instance._plugin.set.assert_called_once_with(key, value)
