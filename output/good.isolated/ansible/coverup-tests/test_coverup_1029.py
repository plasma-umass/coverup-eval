# file lib/ansible/vars/fact_cache.py:41-42
# lines [41, 42]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

# Assuming the FactCache class is part of a larger module and has dependencies
# that need to be mocked for isolation.

@pytest.fixture
def fact_cache(mocker):
    plugin_mock = mocker.MagicMock()
    fact_cache_instance = FactCache()
    mocker.patch.object(fact_cache_instance, '_plugin', new=plugin_mock)
    return fact_cache_instance, plugin_mock

def test_fact_cache_contains(fact_cache):
    fact_cache_instance, plugin_mock = fact_cache
    # Setup: Define a key to test
    test_key = 'test_key'
    
    # Mock the plugin's contains method to return True for the test_key
    plugin_mock.contains.return_value = True
    
    # Test: Check if the key is in the fact cache
    assert test_key in fact_cache_instance
    
    # Verify that the plugin's contains method was called with the correct key
    plugin_mock.contains.assert_called_once_with(test_key)
    
    # Cleanup is handled by the fixture's scope and pytest's garbage collection
