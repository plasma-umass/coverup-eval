# file lib/ansible/vars/fact_cache.py:50-52
# lines [50, 52]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

class MockFactCache(FactCache):
    def __init__(self, *args, **kwargs):
        super(MockFactCache, self).__init__(*args, **kwargs)
        self.store = {}

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def copy(self):
        """ Return a primitive copy of the keys and values from the cache. """
        return dict(self.store)  # Override to copy from the internal store

@pytest.fixture
def fact_cache():
    return MockFactCache()

def test_fact_cache_copy(fact_cache):
    # Setup the fact cache with some values
    fact_cache['key1'] = 'value1'
    fact_cache['key2'] = 'value2'

    # Perform the copy operation
    copied_cache = fact_cache.copy()

    # Assert that the copied cache is a dictionary with the correct items
    assert isinstance(copied_cache, dict)
    assert copied_cache == {'key1': 'value1', 'key2': 'value2'}  # Compare with the expected dictionary

    # Clean up the fact cache
    del fact_cache['key1']
    del fact_cache['key2']
