# file: lib/ansible/plugins/filter/urlsplit.py:29-35
# asked: {"lines": [29, 30, 32, 33, 34], "branches": []}
# gained: {"lines": [29, 30, 32, 33, 34], "branches": []}

import pytest
from ansible.plugins.filter.urlsplit import FilterModule, split_url

def test_filter_module_filters(monkeypatch):
    # Create an instance of the FilterModule
    filter_module = FilterModule()
    
    # Get the filters dictionary
    filters = filter_module.filters()
    
    # Assert that 'urlsplit' is in the filters dictionary and points to the correct function
    assert 'urlsplit' in filters
    assert filters['urlsplit'] == split_url
