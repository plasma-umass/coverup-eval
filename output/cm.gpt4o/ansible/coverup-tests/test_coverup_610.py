# file lib/ansible/plugins/filter/urlsplit.py:29-35
# lines [29, 30, 32, 33, 34]
# branches []

import pytest
from ansible.plugins.filter.urlsplit import FilterModule

def test_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urlsplit' in filters
    assert callable(filters['urlsplit'])
