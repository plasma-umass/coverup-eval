# file lib/ansible/vars/fact_cache.py:50-52
# lines [52]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

# Assuming FactCache is a subclass of MutableMapping and has the necessary methods implemented

def test_fact_cache_copy(mocker):
    # Create a mock FactCache instance with some data
    fact_cache = FactCache()
    fact_cache['key1'] = 'value1'
    fact_cache['key2'] = 'value2'

    # Call the copy method
    copy_result = fact_cache.copy()

    # Assert that the result is a dictionary with the correct items
    assert copy_result == {'key1': 'value1', 'key2': 'value2'}, "The copy method did not return the expected dictionary"
