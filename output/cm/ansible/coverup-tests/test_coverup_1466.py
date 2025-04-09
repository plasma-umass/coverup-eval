# file lib/ansible/vars/fact_cache.py:47-48
# lines [48]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

# Assuming FactCache is a subclass of MutableMapping and has a _plugin attribute
# that is a dict-like object with a keys method.

class MockPlugin:
    def __init__(self):
        self.data = {}

    def keys(self):
        return self.data.keys()

@pytest.fixture
def fact_cache(mocker):
    plugin = MockPlugin()
    fact_cache_instance = FactCache()
    mocker.patch.object(fact_cache_instance, '_plugin', new=plugin)
    return fact_cache_instance

def test_fact_cache_len(fact_cache):
    # Initially, the length should be 0
    assert len(fact_cache) == 0

    # Add a key to the mock plugin to simulate stored facts
    fact_cache._plugin.data['test_key'] = 'test_value'

    # Now, the length should be 1
    assert len(fact_cache) == 1

    # Clean up by removing the key
    del fact_cache._plugin.data['test_key']

    # Length should be back to 0
    assert len(fact_cache) == 0
