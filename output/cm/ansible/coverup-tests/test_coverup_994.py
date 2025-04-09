# file lib/ansible/vars/fact_cache.py:38-39
# lines [38, 39]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache
from unittest.mock import MagicMock

@pytest.fixture
def fact_cache():
    cache = FactCache()
    cache._plugin = MagicMock()
    return cache

def test_fact_cache_delitem(fact_cache):
    # Set up the key to be deleted
    key_to_delete = 'test_key'
    
    # Call __delitem__ which should trigger the plugin's delete method
    fact_cache.__delitem__(key_to_delete)
    
    # Assert that the plugin's delete method was called with the correct key
    fact_cache._plugin.delete.assert_called_once_with(key_to_delete)
