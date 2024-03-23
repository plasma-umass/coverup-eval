# file lib/ansible/plugins/cache/memory.py:23-53
# lines [23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53]
# branches []

import pytest
from ansible.plugins.cache.memory import CacheModule

@pytest.fixture
def cache_module():
    return CacheModule()

def test_cache_module_set_get(cache_module):
    # Test set and get methods
    cache_module.set('key1', 'value1')
    assert cache_module.get('key1') == 'value1'

    # Test keys method
    assert 'key1' in cache_module.keys()

    # Test contains method
    assert cache_module.contains('key1') is True
    assert cache_module.contains('nonexistent_key') is False

    # Test delete method
    cache_module.delete('key1')
    assert cache_module.get('key1') is None

    # Test flush method
    cache_module.set('key2', 'value2')
    cache_module.flush()
    assert cache_module.get('key2') is None

    # Test __getstate__ and __setstate__ methods
    cache_module.set('key3', 'value3')
    state = cache_module.__getstate__()
    assert state == {'key3': 'value3'}

    new_cache_module = CacheModule()
    new_cache_module.__setstate__(state)
    assert new_cache_module.get('key3') == 'value3'
