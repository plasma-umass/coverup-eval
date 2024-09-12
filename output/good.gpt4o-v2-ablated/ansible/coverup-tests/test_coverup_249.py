# file: lib/ansible/plugins/filter/urlsplit.py:29-35
# asked: {"lines": [29, 30, 32, 33, 34], "branches": []}
# gained: {"lines": [29, 30, 32, 33, 34], "branches": []}

import pytest
from ansible.plugins.filter.urlsplit import FilterModule

def test_filter_module_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urlsplit' in filters
    assert callable(filters['urlsplit'])
