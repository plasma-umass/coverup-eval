# file: lib/ansible/plugins/cache/memory.py:23-53
# asked: {"lines": [23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53], "branches": []}
# gained: {"lines": [23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53], "branches": []}

import pytest
from ansible.plugins.cache.memory import CacheModule

@pytest.fixture
def cache():
    return CacheModule()

def test_cache_init(cache):
    assert cache._cache == {}

def test_cache_get(cache):
    cache.set('key1', 'value1')
    assert cache.get('key1') == 'value1'
    assert cache.get('key2') is None

def test_cache_set(cache):
    cache.set('key1', 'value1')
    assert cache._cache['key1'] == 'value1'

def test_cache_keys(cache):
    cache.set('key1', 'value1')
    cache.set('key2', 'value2')
    assert set(cache.keys()) == {'key1', 'key2'}

def test_cache_contains(cache):
    cache.set('key1', 'value1')
    assert cache.contains('key1') is True
    assert cache.contains('key2') is False

def test_cache_delete(cache):
    cache.set('key1', 'value1')
    cache.delete('key1')
    assert 'key1' not in cache._cache

def test_cache_flush(cache):
    cache.set('key1', 'value1')
    cache.flush()
    assert cache._cache == {}

def test_cache_copy(cache):
    cache.set('key1', 'value1')
    cache_copy = cache.copy()
    assert cache_copy == {'key1': 'value1'}
    assert cache_copy is not cache._cache

def test_cache_getstate(cache):
    cache.set('key1', 'value1')
    state = cache.__getstate__()
    assert state == {'key1': 'value1'}

def test_cache_setstate(cache):
    state = {'key1': 'value1'}
    cache.__setstate__(state)
    assert cache._cache == state
