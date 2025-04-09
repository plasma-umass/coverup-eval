# file lib/ansible/plugins/filter/urlsplit.py:29-35
# lines [29, 30, 32, 33, 34]
# branches []

import pytest
from ansible.plugins.filter.urlsplit import FilterModule

def test_urlsplit_filter():
    filter_module = FilterModule()
    filters_dict = filter_module.filters()
    assert 'urlsplit' in filters_dict
    assert filters_dict['urlsplit'].__name__ == 'split_url'
